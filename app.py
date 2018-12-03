import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt, mpld3
from flask import Flask, send_file, json, render_template
import praw
from wordOps import countWords, punctRm, excludeWordsList, totalKarmaOfWords
from config import RedditConfig

# Send "public/any.name" when route "<site>.com/{any.name}" is hit
app = Flask(__name__, static_url_path="", static_folder="static", template_folder='templates')
import errors

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
	Please use the search bar to navigate to see more.
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
	#Here is likely where you want to figure out karma of words
	#totalKarmaOfWords(sortedWords, submissions)
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
		plt.subplot(1, 2, 2) #made it =ax
		text = str(sortedWords)
		text = text.replace("'", "")
		wordcloud = WordCloud(width=1000, height=1000, margin=0).generate(text)
		plt.imshow(wordcloud, interpolation='bilinear')
		plt.axis("off")
		plt.margins(x=0, y=0)
		
	else:
		plt.text(0.5,0.5,'There are no posts for the selected search.\nDid you mean to search for /r?', horizontalalignment='center', verticalalignment='center')

	#top post by subreddit
	result=mpld3.fig_to_html(fig)
	result+="<div style='width: 100%; overflow: hidden;' class='comment' >"
	result+="<div style='width:75%; float: left;'> <h3> Top Post in: r/" +str(subreddit)
	result+= " With a score of: " + str(next(funct(subreddit)).score) + "</h3> <p> <h3> User: u/" + str(next(funct(subreddit)).author) + "</h3>"
	result+= "<h3> Title: </h3> <p>'"+ next(funct(subreddit)).title+ "'</p> </div>"
	result+= "</div>"
	
	#made result object to make it easier to build output
	return render_template('index.html', chart=result)


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
	subredditStrings = list()
	for comment in commentWords:
		usersText.append(comment.body)
		subredditStrings.append(str(comment.subreddit))
	for sub in submissionWords:
		usersText.append(sub.selftext)
		subredditStrings.append(str(sub.subreddit))
	sortedWords = countWords(usersText, punctRm, excludeWordsList)
	sortedWords = sortedWords[:50]
	#Here is likely where you want to figure out karma of words
	#totalKarmaOfWords(sortedWords, submissions)
	labels = list()
	values = list()
	for word in sortedWords:
		labels.append(word[0])
		values.append(word[1])

	sortedSubreddits = countWords(subredditStrings, "~", [""])
	srLabels = list()
	srValues = list()
	for word in sortedSubreddits:
		srLabels.append(word[0])
		srValues.append(word[1])
	
	fig = plt.figure()
	if sortedWords:
		
		# Generate Chart
		plt.subplot(3, 1, 2)
		plt.bar(range(len(labels)), values, tick_label=labels)
		ax1 = fig.add_subplot(312)
		fig.subplots_adjust(top=0.85)
		ax1.set_xlabel('Word')
		y_rotate=ax1.set_ylabel('Instances')
		y_rotate.set_rotation(0)
		ax1.set_title('/u/' + str(user))
		
		# Generate Word Cloud
		plt.subplot(3, 1, 1)
		text = str(sortedWords)
		text = text.replace("'", "")
		wordcloud = WordCloud(width=1000, height=1000, margin=0).generate(text)
		plt.imshow(wordcloud, interpolation='bilinear')
		plt.axis("off")
		plt.margins(x=0, y=0)
		
		#Generate plot of subreddits user is active in.
		plt.subplot(3, 1, 3)
		plt.bar(range(len(srLabels)), srValues, tick_label=srLabels)
		ax2 = fig.add_subplot(313)
		#fig.subplots_adjust(top=0.85)
		ax2.set_xlabel('Subreddits')
		y_rotate=ax2.set_ylabel('Posts')
		y_rotate.set_rotation(0)
		ax2.set_title('Posts per Subreddit')

	else:
		plt.text(0.5,0.5,'There are no posts for the selected search.\nDid you mean to search for /r?', horizontalalignment='center', verticalalignment='center')

	
	#top post by user
	result=mpld3.fig_to_html(fig)
	result+="<div style='width: 100%; overflow: hidden;' class='comment'>"
	result+= "<div style='width:100%; float: left;'> <h3>Best Comment of: u/" +str(user) +"</h3>"
	result+= "<h3> Found in: r/"+ comment.subreddit.display_name +" </h3> <p> '" + next(funct(user.comments)).body +"' </p> </div>"
	result+= "</div>"
	
	#made result object to make it easier to build output
	return render_template('index.html', chart=result)
