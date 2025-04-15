from typing import List
import db.conn
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from db.models import Animal, Genotype, Breed, Tag

class DropdownOption:
    def __init__(self, id: int, value: str):
        self.id = id
        self.value = value

async def get_options(datasource: str, session: Session = Depends(db.conn.get_db)) -> List[DropdownOption]:
    type = Animal;
    match datasource:
        case 'genotype':
            type = Genotype
        case 'breed':
            type = Breed
        case 'tag':
            type = Tag

    return [DropdownOption(option.id, getattr(option, datasource)) for option in session.scalars(select(type)).all()]
