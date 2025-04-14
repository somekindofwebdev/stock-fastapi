from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db, json, datasources

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # allows specific origins
    allow_credentials=True,
    allow_methods=["*"],               # allows all HTTP methods
    allow_headers=["*"],               # allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/options/{datasource}")
def read_item(datasource: str):
    return datasources.get_options(datasource)

@app.get("/animals")
def get_animals():
    animals = col_names = None
    try:
        cur = db.get_db().cursor()
        cur.execute(get_query())
        animals = cur.fetchall()
        col_names = [col.name for col in cur.description or []]
        cur.close()
    except Exception as e:
        return { 'error': 1, 'message': str(e) }

    return { 'headers': col_names, 'data': animals }

def get_query():
    return '''select
	animals.id "Animal ID",
	genotypes.genotype "Genotype",
	breeds.breed "Breed",
	tags.tag_no "Tag No."
    from
	animals
	left join genotypes on genotype_id = genotypes.id
	left join breeds on breed_id = breeds.id
	left join tags on tag_id = tags.id'''
