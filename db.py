import os, psycopg
from dotenv import load_dotenv

load_dotenv()

def get_db():

    return psycopg.connect(
        # current_app.config['DATABASE'],
        host='localhost',
        dbname='stock',
        user=os.getenv('DB_USERNAME', 'stock'),
        password=os.getenv('DB_PASSWORD')
    )
