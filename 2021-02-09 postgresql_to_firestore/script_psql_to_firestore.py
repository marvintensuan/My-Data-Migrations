'''
Move data from Google Cloud SQL to Google Firestore.

Author: Marvin D. Tensuan

Related repository: https://github.com/marvintensuan/cv-django
'''

from Connection import * #pylint: disable=unused-wildcard-import
from env_load_env_variables import PSQL_CONN_ARG
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

FOR_UPLOAD = dict.fromkeys([COLLECTION_NAMES)

def get_table_from_Cloud_SQL(table_name):
    db.execute(f'SELECT * from {table_name}')
    col_names = db.table_headers()
    
    table_data = db.fetchall()

    data_list = list_of_dictionaries(col_names, table_data)
    return data_list



# cur.execute('SELECT * FROM mt_backend_cpd;')

# Close database connection.
db.close()
