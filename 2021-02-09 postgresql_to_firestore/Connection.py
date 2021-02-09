'''
Connection class is an instance of a Postgresql connection.
'''

from dataclasses import make_dataclass, asdict
import psycopg2

class Connection:
    '''Postgresql database connection.'''
    def __init__(self, connection_details):
        self.conn = psycopg2.connect(connection_details)
        self.cur = self.conn.cursor()
        self.__table_headers = []

    def close(self):
        self.conn.close()
        self.cur.close()

    def execute(self, query):
        self.__table_headers = []
        return self.cur.execute(query)

    def fetchall(self):
        return self.cur.fetchall()

    def table_headers(self):
        '''
        psycopg2.cursor.description is a sequence of seven `Column` instances.
        See documentation for psycopg2.cursor: https://www.psycopg.org/docs/cursor.html
        '''
        for Column in self.cur.description:
            self.__table_headers.append(Column[0])
        return self.__table_headers

    def dataclass_from_schema(self, class_name):
        '''Create a dataclass based on a table schema from Postgresql.'''
        return make_dataclass(class_name, self.__table_headers)
    
    @staticmethod
    def to_dict(dataclass):
        return asdict(dataclass)