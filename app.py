from flask import Flask
import praw
from config import RedditConfig

app = Flask(__name__)

reddit = praw.Reddit(client_id=RedditConfig.id,
                     client_secret=RedditConfig.secret,
                     user_agent=RedditConfig.userAgent)

@app.route('/')
def index():
    return 'The future home of InTheLoop'

