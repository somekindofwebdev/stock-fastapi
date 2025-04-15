import db
from sqlalchemy.orm import Session
from fastapi import Depends
from db.models import Breed

def check_genotype(breed, genotype, session: Session = Depends(db.conn.get_db)):
    query = session.query(Breed).where(Breed.id == breed).where(Breed.genotype == genotype)

    return bool(session.scalars(query).one())
