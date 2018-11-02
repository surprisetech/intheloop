import matplotlib.pyplot as plt, mpld3
from flask import Flask, send_file, json, render_template
import praw
from wordOps import countWords, punctRm, excludeWordsList
from config import RedditConfig

# Send "public/any.name" when route "<site>.com/{any.name}" is hit
app = Flask(__name__, static_url_path="", static_folder="static", template_folder='templates')

# Initialize PRAW (reddit wrapper) from config.py
# DO NOT push config.py to github, we do not want to
# make the API keys public.
# The format of config.py is:
#
# class RedditConfig:
#     id = '<client_id>'
#     secret = '<client_secret>'
#     userAgent = '<user_agent>'
reddit = praw.Reddit(client_id=RedditConfig.id,
                     client_secret=RedditConfig.secret,
                     user_agent=RedditConfig.userAgent)


# Remap '/' to index. Other files can be served statically.
@app.route('/')
def index():
	return render_template('index.html', chart="""
	Welcome to Seeing Redd. 
	Please navigate to 
	<a>/r/{subreddit-name}/hot</a>
	or
	<a>/u/{username}</a>
	to see more.
	""")

def newPosts(sr):
	return reddit.subreddit(sr).new(limit=100)

def hotPosts(sr):
	return reddit.subreddit(sr).hot(limit=100)

def topPostsAllTime(sr):
	return reddit.subreddit(sr).top(time_filter='all', limit=100)
	
def topPostsPast24Hours(sr):
	return reddit.subreddit(sr).top(time_filter='day', limit=100)	

def controversalPostsAllTime(sr):
	return reddit.subreddit(sr).controversial(time_filter = 'all', limit=100)
	
def controversalPast24Hours(sr):
	return reddit.subreddit(sr).controversial(time_filter = 'day', limit=100)


@app.route('/r/<sr>/<category>/')
def wordCountSubreddit(sr, category):
	switch = {"new":newPosts(sr),
			   "hot":hotPosts(sr),
			   "topalltime":topPostsAllTime(sr),
			   "top24hrs":topPostsPast24Hours(sr),
			   "controversalall":controversalPast24Hours(sr),
			   "controversal24hrs":controversalPast24Hours(sr),
	}
	submissions = switch.get(category)
	posts = list(map(lambda x: x.selftext + " " + x.title, submissions))
	sortedWords = countWords(posts, punctRm, excludeWordsList)
	sortedWords = sortedWords[:50]
	labels = list()
	values = list()
	for word in sortedWords:
		labels.append(word[0])
		values.append(word[1])

	# Generate chart.
	fig = plt.figure()
	plt.bar(range(len(labels)), values, tick_label=labels)

	return render_template('index.html', chart=mpld3.fig_to_html(fig))

#word popularity by user-KT
@app.route('/u/<user>/')
def wordCountUser(user):
	user = reddit.redditor(name=user)
	comments = user.comments.hot(limit=100)
	submissions = user.submissions.hot(limit=100)

	usersText = list()
	for comment in comments:
		usersText.append(comment.body)

	for sub in submissions:
		usersText.append(sub.selftext)

	sortedWords = countWords(usersText, punctRm, excludeWordsList)
	sortedWords = sortedWords[:50]
	labels = list()
	values = list()
	for word in sortedWords:
		labels.append(word[0])
		values.append(word[1])

	# Generate chart.
	fig = plt.figure()
	plt.bar(range(len(labels)), values, tick_label=labels)

	return render_template('index.html', chart=mpld3.fig_to_html(fig))
