import os
from dotenv import load_dotenv

load_dotenv()

db = os.getenv('db')
user = os.getenv('user')
pw = os.getenv('password')

PSQL_CONN_ARG = f'dbname={db} user={user} password={pw}'
