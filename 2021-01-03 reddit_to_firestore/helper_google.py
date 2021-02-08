import os
from datetime import datetime

def GOOGLE_APPLICATION_CREDENTIALS():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "projects-service_account.json"

def upload_to_firestore(date, url, subreddit, body):
    return {
        'date': datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:%S"),
        'url': url,
        'subreddit': subreddit,
        'body': body
    }
