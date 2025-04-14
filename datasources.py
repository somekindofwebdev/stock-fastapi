import db

def get_options(datasource: str):
    options = None
    try:
        cur = db.get_db().cursor()
        cur.execute(get_options_query(datasource))
        options = cur.fetchall()
        cur.close()
    except Exception as e:
        return { 'error': 1, 'message': str(e) }

    return { 'options': options }

def get_options_query(datasource: str):
    return 'select id, {0} from {0}s'.format(datasource)
    # if (filter_table):
    #     query += ' JOIN {1}s ON {0}s.{1}_id = {1}s.id'.format(datasource)
