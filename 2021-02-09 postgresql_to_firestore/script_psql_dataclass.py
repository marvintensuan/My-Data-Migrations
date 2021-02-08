'''
Helper functions for the main script.
'''

from dataclasses import make_dataclass, asdict
import psycopg2

def dataclass_from_schema(from_table, table_schema):
    '''Create a dataclass based on a table schema from Postgresql.'''
    return make_dataclass(from_table, [name for name, _ in table_schema])