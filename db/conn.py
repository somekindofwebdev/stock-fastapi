import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import URL

load_dotenv()

def get_db():
    url_object = URL.create(
        'postgresql+psycopg',
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host='localhost',
        database='stock',
    )
    return create_engine(url_object, echo=True)
