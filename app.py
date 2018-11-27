import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt, mpld3
from flask import Flask, send_file, json, render_template
import praw
from wordOps import countWords, punctRm, excludeWordsList
import os
import config

# Send "public/any.name" when route "<site>.com/{any.name}" is hit
app = Flask(__name__, static_url_path="", static_folder="static", template_folder='templates')
import errors

# Initialize PRAW (reddit wrapper) from config.py
# DO NOT push config.py to github, we do not want to
# make the API keys public.
reddit = praw.Reddit(client_id=os.environ["praw_id"],
                     client_secret=os.environ["praw_secret"],
                     user_agent=os.environ["praw_agent"])

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

def newPosts(searchbase):
	return searchbase.new(limit=100)

def hotPosts(searchbase):
	return searchbase.hot(limit=100)

def topPostsAllTime(searchbase):
	return searchbase.top(time_filter='all', limit=100)
	
def topPostsPast24Hours(searchbase):
	return searchbase.top(time_filter='day', limit=100)

def controversialPostsAllTime(searchbase):
	return searchbase.controversial(time_filter='all', limit=100)
	
def controversialPast24Hours(searchbase):
	return searchbase.controversial(time_filter='day', limit=100)

switch = {"new": lambda x: newPosts(x),
		  "hot": lambda x: hotPosts(x),
		  "topalltime": lambda x: topPostsAllTime(x),
		  "top24hrs": lambda x: topPostsPast24Hours(x),
		  "controversialall": lambda x: controversialPostsAllTime(x),
		  "controversial24hrs": lambda x: controversialPast24Hours(x),
		  #how can we refactor these to work with the changes in the index function?
}

@app.route('/r/<sr>/contributors/<category>')
def contributorsToSubreddit(sr, category):
	funct = switch.get(category)
	subreddit = reddit.subreddit(sr)
	submissions = funct(subreddit)
	contributers = filter(lambda x: x != None, [x.author for x in submissions])
	return render_template('index.html', data=contributers)

@app.route('/r/<sr>/<category>')
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

	fig = plt.figure()
	if sortedWords:
	# Generate Chart
		plt.subplot(1, 2, 1)
		plt.bar(range(len(labels)), values, tick_label=labels)
		ax1 = fig.add_subplot(121)
		fig.subplots_adjust(top=0.85)
		ax1.set_xlabel('Word')
		y_rotate=ax1.set_ylabel('Instances')
		y_rotate.set_rotation(0)
		ax1.set_title('/r/' + str(subreddit))
	# Generate Word Cloud
		plt.subplot(1, 2, 2)
		text = str(sortedWords)
		text = text.replace("'", "")
		wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
		plt.imshow(wordcloud, interpolation='bilinear')
		plt.axis("off")
		plt.margins(x=0, y=0)
	else:
		plt.text(0.5,0.5,'There are no posts for the selected search.')
		#can make this route to one of the error pages
		#or have it suggest similar search like /u instead of /r etc

	return render_template('index.html', chart=mpld3.fig_to_html(fig))

#Compare words user posts in a subreddit to their other subreddits
@app.route('/c/<user>/<sr>/<category>')
def compareUserReddits(user, sr, category):
        funct = switch.get(category)
        subreddit = reddit.subreddit(sr)
        submissions = funct(subreddit)
        posts = list()
        for i in submissions:
                if i.author.name == user:
                        posts.append(i.selftext + " " + i.title)

        return posts[0]

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
	
	fig = plt.figure()
	if sortedWords:
	# Generate Chart
		plt.subplot(1, 2, 1)
		plt.bar(range(len(labels)), values, tick_label=labels)
		ax1 = fig.add_subplot(121)
		fig.subplots_adjust(top=0.85)
		ax1.set_xlabel('Word')
		y_rotate=ax1.set_ylabel('Instances')
		y_rotate.set_rotation(0)
		ax1.set_title('/u/' + str(user))
	# Generate Word Cloud
		plt.subplot(1, 2, 2)
		text = str(sortedWords)
		text = text.replace("'", "")
		wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
		plt.imshow(wordcloud, interpolation='bilinear')
		plt.axis("off")
		plt.margins(x=0, y=0)
	else:
		plt.text(0.5,0.5,'There are no posts for the selected search.')
		#can make this route to one of the error pages
		#or have it suggest similar search like /u instead of /r etc

	return render_template('index.html', chart=mpld3.fig_to_html(fig))
