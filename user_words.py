import praw
from config import RedditConfig

reddit = praw.Reddit(client_id=RedditConfig.id,
                     client_secret=RedditConfig.secret,
                     user_agent=RedditConfig.userAgent)

user = reddit.redditor(name="spez")

print(dir(user))

posts = user.comments.new(limit=100)

for comment in posts:
    print(dir(comment))
    break

for comment in posts:
    print(comment.body)

# parse words