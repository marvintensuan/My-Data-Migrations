def list_of_dictionaries(column_names, table):
    '''Convert each row of the table into dictionaries then put them all in a list.'''
    data_list = []
    for row in table:
        data_list.append(dict(zip(column_names, row)))
    return data_list