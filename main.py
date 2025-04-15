from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import List
from db.models import Animal, Genotype, Breed, Tag
from responses.schemas import AnimalOut, DropdownOptionOut
from datasources import DropdownOption
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


@app.get("/options/{datasource}", response_model=List[DropdownOptionOut])
def read_item(datasource: str) -> List[DropdownOption]:
    return datasources.get_options(datasource)

@app.get("/animals", response_model=List[AnimalOut])
async def get_animals() -> List[Animal]:
    session = Session(db.conn.get_db())
    query = (
        select(Animal.id, Genotype.genotype, Breed.breed, Tag.tag_no)
        .select_from(Animal)
        .join(Genotype, Animal.genotype_id == Genotype.id)
        .join(Breed, Animal.breed_id == Breed.id)
        .join(Tag)
        .order_by(Animal.id)
    )

    return session.execute(query).all()

    #     return { 'error': 1, 'message': str(e) }

# @app.post("/animals")
# def add_animal(animal: Animal):
#     if not validation.check_genotype(animal.breed, animal.genotype):
#         return "{0} is not a type of {1}".format(animal.breed, animal.genotype)
