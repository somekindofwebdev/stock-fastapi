import os, psycopg

def get_db():
    return psycopg.connect(
        # current_app.config['DATABASE'],
        host='localhost',
        dbname='stock',
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
