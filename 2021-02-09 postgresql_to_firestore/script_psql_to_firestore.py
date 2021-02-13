'''
Move data from Google Cloud SQL to Google Firestore.
Each table will be entitled to a single Firestore Collection,
and each row will be its own document.

Author: Marvin D. Tensuan

Related repository: https://github.com/marvintensuan/cv-django
'''

from Connection import Connection
from env_load_env_variables import PSQL_CONN_ARG
from google.cloud import firestore
from helper import *

# Initialize database connection
db = Connection(PSQL_CONN_ARG)

TABLE_NAMES = [
    'mt_backend_cpd',
    'mt_backend_sdl_onlinecourse',
    'mt_backend_sdl_webinars'
]

COLLECTION_NAMES = [
    i.replace('mt_backend', 'flaskapp2')
    for i in TABLE_NAMES
]

FOR_UPLOAD = dict.fromkeys(COLLECTION_NAMES)

def convert_table_from_Cloud_SQL(table_name):
    # Execute query in a database
    db.execute(f'SELECT * from {table_name};')

    # Extract column names and data; then run through `helper.list_of_dictionaries`
    col_names = db.table_headers()
    table_data = db.fetchall()
    return list_of_dictionaries(col_names, table_data)


for collection, table in zip(COLLECTION_NAMES, TABLE_NAMES):
    FOR_UPLOAD[collection] = convert_table_from_Cloud_SQL(table)

# Close database connection.
db.close()

# TODO: Upload to Firestore.
