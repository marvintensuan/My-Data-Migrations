from script_psql_to_firestore import rand_string

test_cases = [5, 5.0, 'abc']

for case in test_cases:
    try:
        print(rand_string(case))
    except TypeError:
        print('Type error:', type(case))