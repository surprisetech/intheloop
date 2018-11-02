import string
import matplotlib.pyplot as plt, mpld3
from flask import Flask, send_file, json, render_template
import praw
from wordOps import countWords
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
	print("newPosts")
	if(searchbase2 is not None):
			comments = searchbase.new(limit=100)
			submissions = searchbase2.new(limit=100)
			usersText = list()
			for comment in comments:
				usersText.append(comment.body)

			for sub in submissions:
				usersText.append(sub.selftext)
			return usersText
	else:
		return searchbase.new(limit=100)

def hotPosts(searchbase, searchbase2 = None):
	print("hotPosts")
	if(searchbase2 is not None):
			comments = searchbase.hot(limit=100)
			submissions = searchbase2.hot(limit=100)
			usersText = list()
			for comment in comments:
				usersText.append(comment.body)

			for sub in submissions:
				usersText.append(sub.selftext)
			return usersText
	else:
		return searchbase.hot(limit=100)

def topPostsAllTime(searchbase, searchbase2 = None):
	print("topPostsAllTime")
	if(searchbase2 is not None):
			comments = searchbase.top(time_filter='all', limit=100)
			submissions = searchbase2.top(time_filter='all', limit=100)
			usersText = list()
			for comment in comments:
				usersText.append(comment.body)

			for sub in submissions:
				usersText.append(sub.selftext)
			return usersText
	else:
		return searchbase.new(time_filter='all', limit=100)
	
def topPostsPast24Hours(searchbase, searchbase2 = None):
	print("topPostsPast24Hours")
	if(searchbase2 is not None):
			comments = searchbase.top(time_filter='day', limit=100)
			submissions = searchbase2.top(time_filter='day', limit=100)
			usersText = list()
			for comment in comments:
				usersText.append(comment.body)

			for sub in submissions:
				usersText.append(sub.selftext)
			return usersText
	else:
		return searchbase.new(time_filter='day', limit=100)

def controversalPostsAllTime(searchbase, searchbase2 = None):
	print("controversalPostsAllTime")
	if(searchbase2 is not None):
			comments = searchbase.controversalall(time_filter='all', limit=100)
			submissions = searchbase2.controversalall(time_filter='all', limit=100)
			usersText = list()
			for comment in comments:
				usersText.append(comment.body)

			for sub in submissions:
				usersText.append(sub.selftext)
			return usersText
	else:
		return searchbase.controversial(time_filter='all', limit=100)
	
def controversalPast24Hours(searchbase, searchbase2 = None):
	print("controversalPast24Hours")
	if(searchbase2 is not None):
			comments = searchbase.controversalall(time_filter='day', limit=100)
			submissions = searchbase2.controversalall(time_filter='day', limit=100)
			usersText = list()
			for comment in comments:
				usersText.append(comment.body)

			for sub in submissions:
				usersText.append(sub.selftext)
			return usersText
	else:
		return searchbase.controversial(time_filter='day', limit=100)

def creepOnUser(user):
	return

switch = {"new": lambda x,y=None: newPosts(x,y),
		  "hot": lambda x,y=None: hotPosts(x,y),
		  "topalltime": lambda x,y=None: topPostsAllTime(x,y),
		  "top24hrs": lambda x,y=None: topPostsPast24Hours(x,y),
		  "controversalall": lambda x,y=None: controversalPast24Hours(x,y),
		  "controversal24hrs": lambda x,y=None: controversalPast24Hours(x,y),
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

	return render_template('index.html', chart=mpld3.fig_to_html(fig))

#word popularity by user-KT
@app.route('/u/<user>/<category>')
def wordCountUser(user):
	user = reddit.redditor(name=user)
	comments = user.comments
	submissions = user.submissions
	funct = switch.get(category)
	usersText = funct(comments, submissions)
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


punctRm = str.maketrans('', '', string.punctuation + "“”’")
excludeWordsList = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on',
                    'at', 'to', 'from', 'by', 'we', 'of', 'as', 'do', 'up', 'if', 'i', 'you', 'are', 'they',
                    'it', 'our', 'be', 'is', 'in', 'my', 'with', 'have', 'has', 'no', 'how', 'was', 'very',
                    'this', 'he', 'that', 'it\'s', 'cunt', 'fuck', 'like', 'not', 'your', 'don\'t', 'she',
                    'his', 'her', 'just', 'when', 'so', 'got', 'get', 'what', 'why', 'who', 'how', 'would',
                    'should', 'could', 'some', 'can', 'you\'re', 'about', 'which', 'had', 'want', 'made']
