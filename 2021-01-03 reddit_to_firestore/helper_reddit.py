import praw
from praw.models import Redditor

def CreateRedditor(user_name: str):
    reddit = praw.Reddit("scraper_tool",
                    user_agent='Python 3.8')
    return Redditor(reddit, user_name)

def get_reddit_comments(user_name: str, lim: int):
    redditor = CreateRedditor(user_name)
    return [comment for comment in redditor.comments.new(limit=lim)]

def get_reddit_submissions(user_name: str, lim: int):
    redditor = CreateRedditor(user_name)
    return [submission for submission in redditor.submissions.new(limit=lim)]