import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    password = Column(String(250))
    email = Column(String(250))

class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    race = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))
    population = Column(String(250))
    img = Column(String(250))

class Fav_people(Base):
    __tablename__ = 'fav_people'

    id = Column(Integer, primary_key=True)
    id_people = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    name = Column(String(250))
    description = Column(String(250))

class Fav_planets(Base):
    __tablename__ = 'fav_planets'

    id = Column(Integer, primary_key=True)
    id_planets = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    id_user = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    name = Column(String(250))
    description = Column(String(250))






render_er(Base, 'diagram.png')
