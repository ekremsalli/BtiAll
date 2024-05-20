
def convert_dict_to_sql_where_clause(data):
    clause = []
    for key, value in data.items():
        if value:
            if isinstance(value, tuple):
                op, val = value
                clause.append(f'{key}{op}\'{val}\'')
            else:
                clause.append(f'{key}=\'{value}\'')
    return str.join(' AND ', clause)


def dict_fetch_all(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d
