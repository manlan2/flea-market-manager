from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Owner(Base):
    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))



class Booths(Base):
    __tablename__ = 'booths'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    image = Column(String(250))
    email = Column(String(250))
    phone = Column(String(16))
    owner_id = Column(Integer, ForeignKey('owner.id'))
    owner = relationship(Owner)

    @property
    def serialize(self):
        """ Add comment here """
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'email': self.email,
            'phone': self.phone,
            'owner_id': self.owner_id
        }



class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    category = Column(String(80))
    image = Column(String(250))
    booth_id = Column(Integer, ForeignKey('booths.id'))
    booths = relationship(Booths)
    owner_id = Column(Integer, ForeignKey('owner.id'))
    owner = relationship(Owner)


    @property
    def serialize(self):
        ''' Add comment here '''
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'booth_id': self.booth_id,
            'image': self.image,
            'owner_id': self.owner_id
        }


engine = create_engine('sqlite:///fleamarket.db')


Base.metadata.create_all(engine)
