from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

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
    genotype: Mapped[List["Genotype"]] = relationship(
        back_populates="genotypes", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Breed(id={self.id!r}, breed={self.breed!r}, genotype={self.genotype!r})"

class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    tag_no: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Tag(id={self.id!r}, tag_no={self.tag_no!r})"


class Animal(Base):
    __tablename__ = "animals"

    id: Mapped[int] = mapped_column(primary_key=True)
    genotype: Mapped[List["Genotype"]] = relationship(
        back_populates="genotypes", cascade="all, delete-orphan"
    )
    breed: Mapped[List["Breed"]] = relationship(
        back_populates="breeds", cascade="all, delete-orphan"
    )
    tag: Mapped[List["Tag"]] = relationship(
        back_populates="tags", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Animal(id={self.id!r}, genotype={self.genotype!r}, breed_id={self.breed!r}, tag_id={self.tag!r})"
