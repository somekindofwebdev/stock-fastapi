from typing import List
import db.conn
from sqlalchemy import select
from sqlalchemy.orm import Session
from db.models import Animal, Genotype, Breed, Tag

class DropdownOption:
    id: int
    value: str
    def __init__(self, id: int, value: str):
        self.id = id
        self.value = value

def get_options(datasource: str):# -> List[DropdownOption]:
    session = Session(db.conn.get_db())
    type = Animal;
    match datasource:
        case 'genotype':
            type = Genotype
        case 'breed':
            type = Breed
        case 'tag':
            type = Tag


    options = session.execute(select(type)).all()
    return [DropdownOption(id=option[0].id, value=getattr(option[0], datasource)) for option in options]
