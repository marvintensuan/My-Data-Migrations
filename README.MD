# My Data Migrations

Repository for scripts used to move data from one source to another.

- **2021-01-03 reddit_to_firestore** &mdash; uses Python Reddit API Wrapper (`praw`) to store my Reddit account information in a Firestore database.
- **2021-02-09 postgresql_to_firestore** &mdash; migrating data from a Cloud SQL Postgresql instance to a Firestore document database. Uses `psycopg2` and `google-cloud` SDK.
	- Related repository: [cv-flask](https://github.com/marvintensuan/cv-flask)