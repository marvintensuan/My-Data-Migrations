from datetime import datetime, time, date
from decimal import Decimal

def list_of_dictionaries(column_names, table):
    '''Convert each row of the table into dictionaries then put them all in a list.'''
    data_list = []
    default_time = time(0,0)
    for row in table:
        # Convert values to native Python data types.
        row_list = list(row)
        for n, item in enumerate(row_list):
            if isinstance(item, date):
                row_list[n] = datetime.combine(item, default_time)
            elif isinstance(item, Decimal):
                row_list[n] = float(item)
        
        # Remove 'id' column
        row_dict = dict(zip(column_names, row_list))
        row_dict.pop('id')
        data_list.append(row_dict)
    return data_list