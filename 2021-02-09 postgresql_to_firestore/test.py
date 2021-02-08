from script_psql_dataclass import *

sample_tuples = (('id', 23),
    ('name', 1043),
    ('thematic', 1043),
    ('units', 1700),
    ('cpd_date', 1082)
)

FROM_SQL = dataclass_from_schema('sample_table', sample_tuples)
a = FROM_SQL(1,2,3,4,5)

print(a)