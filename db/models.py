from typing import List
from sqlalchemy import String, ForeignKey, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

metadata_obj = MetaData()

class Base(DeclarativeBase):
    pass

class Genotype(Base):
    __tablename__ = 'genotypes'

    id: Mapped[int] = mapped_column(primary_key=True)
    genotype: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Genotype(id={self.id!r}, genotype={self.genotype!r})"

class Breed(Base):
    __tablename__ = 'breeds'

    id: Mapped[int] = mapped_column(primary_key=True)
    breed: Mapped[str] = mapped_column(String(255))
    genotype_id: Mapped[int] = mapped_column(ForeignKey('genotypes.id'))

    def __repr__(self) -> str:
        return f"Breed(id={self.id!r}, breed={self.breed!r}, genotype={self.genotype_id!r})"

class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    tag_no: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Tag(id={self.id!r}, tag_no={self.tag_no!r})"


class Animal(Base):
    __tablename__ = "animals"

    id: Mapped[int] = mapped_column(primary_key=True)
    genotype_id: Mapped[int] = mapped_column(ForeignKey('genotypes.id'))
    breed_id: Mapped[int] = mapped_column(ForeignKey('breeds.id'))
    tag_id: Mapped[int] = mapped_column(ForeignKey('tags.id'))

    def __repr__(self) -> str:
        return f"Animal(id={self.id!r}, genotype={self.genotype_id!r}, breed_id={self.breed_id!r}, tag_id={self.tag_id!r})"
