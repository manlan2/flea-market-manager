from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Booths(Base):
    __tablename__ = 'booths'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)



class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    category = Column(String(80))
    booth_id = Column(Integer, ForeignKey('booths.id'))
    booth = relationship(Booths)


engine = create_engine('sqlite:///fleamarket.db')


Base.metadata.create_all(engine)
