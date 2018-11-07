import praw
from config import RedditConfig
    
reddit = praw.Reddit(client_id=RedditConfig.id,
                     client_secret=RedditConfig.secret,
                     user_agent=RedditConfig.userAgent)

user = reddit.redditor(name="spez")

print(dir(user))

posts = user.comments.new(limit=100)

submissions = user.submissions.new(limit=100)

for comment in posts:
    print(dir(comment))
    break

commentText = ""
for comment in posts:
    commentText += comment.body
print(commentText)

subText = ""
for sub in submissions:
    subText += sub.selftext
print(subText)

allWords = commentText + subText
print(allWords)
