import string
from wordcloud import WordCloud
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

def newPosts(searchbase, searchbase2 = None):
	return searchbase.new(limit=100)

def hotPosts(searchbase, searchbase2 = None):
	return searchbase.hot(limit=100)

def topPostsAllTime(searchbase, searchbase2 = None):
	return searchbase.top(time_filter='all', limit=100)
	
def topPostsPast24Hours(searchbase, searchbase2 = None):
	return searchbase.top(time_filter='day', limit=100)

def controversalPostsAllTime(searchbase, searchbase2 = None):
	return searchbase.controversial(time_filter='all', limit=100)
	
def controversalPast24Hours(searchbase, searchbase2 = None):
	return searchbase.controversial(time_filter='day', limit=100)

switch = {"new": lambda x: newPosts(x),
		  "hot": lambda x: hotPosts(x),
		  "topalltime": lambda x: topPostsAllTime(x),
		  "top24hrs": lambda x: topPostsPast24Hours(x),
		  "controversalall": lambda x: controversalPast24Hours(x),
		  "controversal24hrs": lambda x: controversalPast24Hours(x),
}

@app.route('/r/<sr>/<category>/')
def wordCountSubreddit(sr, category):
	funct = switch.get(category)
	subreddit = reddit.subreddit(sr)
	submissions = funct(subreddit)
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
	ax1 = fig.add_subplot(111)
	fig.subplots_adjust(top=0.85)
	ax1.set_xlabel('Word')
	y_rotate=ax1.set_ylabel('Instances')
	y_rotate.set_rotation(0)

	#Generate Word Cloud
	text = str(sortedWords)
	wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.margins(x=0, y=0)
	#plt.show()

	return render_template('index.html', chart=mpld3.fig_to_html(fig))

#word popularity by user
@app.route('/u/<user>/<category>')
def wordCountUser(user, category):
	user = reddit.redditor(name=user)
	comments = user.comments
	submissions = user.submissions
	funct = switch.get(category)
	commentWords = funct(comments)
	submissionWords = funct(submissions)
	usersText = list()
	for comment in commentWords:
		usersText.append(comment.body)
	for sub in submissionWords:
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

	ax1 = fig.add_subplot(111)
	fig.subplots_adjust(top=0.85)
	ax1.set_xlabel('Word')
	y_rotate=ax1.set_ylabel('Instances')
	y_rotate.set_rotation(0)

	#Generate Word Cloud
	text = str(sortedWords)
	wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.margins(x=0, y=0)
	#plt.show()
	return render_template('index.html', chart=mpld3.fig_to_html(fig))
