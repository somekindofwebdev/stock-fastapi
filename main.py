from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, ScalarResult
from sqlalchemy.orm import Session
from typing import List
from db.models import Animal, Genotype, Breed, Tag
from responses.schemas import AnimalOut
import db.conn, datasources, validation

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

@app.get("/animals", response_model=List[AnimalOut])
async def get_animals(session: Session = Depends(db.conn.get_db)) -> List[AnimalOut]:
    query = session.query(Animal).join(Genotype).join(Breed).join(Tag)
    print(query.all())
    return query.all()

    #     return { 'error': 1, 'message': str(e) }

@app.post("/animals")
def add_animal(animal: Animal):
    if not validation.check_genotype(animal.breed, animal.genotype):
        return "{0} is not a type of {1}".format(animal.breed, animal.genotype)

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
