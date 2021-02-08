'''
Move data from Google Cloud SQL to Google Firestore.

Author: Marvin D. Tensuan

Related repository: https://github.com/marvintensuan/cv-django
'''

import psycopg2
from env_load_env_variables import PSQL_CONN_ARG

# Initialize database connection
conn = psycopg2.connect(PSQL_CONN_ARG)
cur = conn.cursor()

TABLE_NAMES = [
    'mt_backend_cpd',
    'mt_backend_sdl_onlinecourse',
    'mt_backend_sdl_webinars'
]

# cur.execute('SELECT * FROM mt_backend_cpd;')

# Close database connection.
cur.close()
conn.close()
