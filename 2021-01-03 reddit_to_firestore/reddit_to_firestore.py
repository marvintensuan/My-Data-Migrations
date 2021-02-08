from google.cloud import firestore

from helper_google import *
from helper_reddit import *

GOOGLE_APPLICATION_CREDENTIALS()
db = firestore.Client()

previous_comments = db.collection('tagapagtuos_comments').stream()
list_of_doc_id = [doc.id for doc in previous_comments]

comments = get_reddit_comments('tagapagtuos', 20)
for comment in comments:
    if comment.id not in list_of_doc_id:
        db.collection('tagapagtuos_comments')   \
            .document(comment.id)               \
            .set(
                upload_to_firestore(
                    comment.created_utc,
                    comment.permalink,
                    comment.subreddit.display_name,
                    comment.body)
            )

previous_submissions = db.collection('tagapagtuos_submissions').stream()
list_of_submissions = [submission.id for submission in previous_submissions]

submissions = get_reddit_submissions('tagapagtuos', 10)
for submission in submissions:
    if submission.id not in list_of_submissions:
            db.collection('tagapagtuos_submissions')   \
                .document(submission.id)               \
                .set(
                    upload_to_firestore(
                        submission.created_utc,
                        submission.permalink,
                        submission.subreddit.display_name,
                        submission.selftext)
                )
