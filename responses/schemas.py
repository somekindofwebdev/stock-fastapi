from pydantic import BaseModel
from db.models import Genotype, Breed, Tag

class AnimalOut(BaseModel):
    id: int
    genotype: Genotype
    breed: Breed
    tag: Tag

    class Config:
        orm_mode = True
