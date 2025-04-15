from pydantic import BaseModel, ConfigDict

class AnimalOut(BaseModel):
    id: int
    genotype: str
    breed: str
    tag_no: str

    model_config = ConfigDict(from_attributes=True)

class DropdownOptionOut(BaseModel):
    id: int
    value: str

    model_config = ConfigDict(from_attributes=True)
