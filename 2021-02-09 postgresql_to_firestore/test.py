from Connection import Connection
from env_load_env_variables import PSQL_CONN_ARG

# SAMPLE USER STORY

SAMPLE_TABLE = 'mt_backend_cpd'

db = Connection(PSQL_CONN_ARG)
db.execute(f'SELECT * from {SAMPLE_TABLE};')

col_names = db.table_headers()
print('TABLE HEADERS:\n', col_names, "\n---------------")

my_dataclass = db.dataclass_from_schema('ClassName')

data = db.fetchall()
print('Raw data:', data[0])

my_dict = {}

for k,v in zip(col_names, data[0]):
    my_dict[k] = v

print(my_dict)
# dc0 = my_dataclass(data[0][0], data[0][1], data[0][2], data[0][3], data[0][4])
# print('As dataclass:', dc0)
# print('As disctionary:\n', db.to_dict(dc0))

db.close()