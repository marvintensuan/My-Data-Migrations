from datetime import datetime, time, date

def list_of_dictionaries(column_names, table):
    '''Convert each row of the table into dictionaries then put them all in a list.'''
    data_list = []
    default_time = time(0,0)
    for row in table:
        row_list = list(row)
        for n, item in enumerate(row_list):
            if isinstance(item, date):
                row_list[n] = datetime.combine(item, default_time)
        data_list.append(dict(zip(column_names, row_list)))
    return data_list