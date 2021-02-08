# Reddit Data Pipeline

## About

The goal of this project is to move data from point A to point B.

## Tech Stack

- Python &mdash; scripting.
- Google Firestore &mdash; cloud document database with free tier.

## Files

**reddit_to_firestore.py** &mdash; move my Reddit account's data to a Firestore database.

Miscellaneous files:

- requirements.txt &mdash; external python modules used.
- projects-service_account.json &mdash; access token required to access Google Firestore (.gitignore)
- praw.ini &mdash; configuration files used by PRAW module to instantiate a Reddit instance. No username and password required. (.gitignore)
- helper-\*.py &mdash; helper functions.

## TODO

- Functionality to move data from Firestore to somewhere else.
- Enforce stricter DRY.

## History

- 2020-01-03 &mdash; Initial commit. Got data from Reddit to Firebase.