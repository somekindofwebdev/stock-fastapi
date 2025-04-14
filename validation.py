import db

def check_genotype(breed, genotype):
    try:
        cur = db.get_db().cursor()
        cur.execute(check_genotype_query(datasource))
        options = cur.fetchone()
        cur.close()
    except Exception as e:
        return { 'error': 1, 'message': str(e) }

    return bool(options)

def check_genotype_query(breed, genotype):
    return 'select * from breeds where id = {0} and genotype_id = {1}'.format(breed, genotype)
