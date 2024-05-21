#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ Reps a City for MySQL database
    Uses SQLAlchemy to link to MySQL cities table

    Attrs:
        __tablename__(str): cities table name
        name (SQLAlchemy str): name of City
        state_id (SQLAlchemy str): FK that links cities to states
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_is = ""
