#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Rep of state object in MySQL db
    Attrs:
        __tablename__(str): states
        name (SQLAlchemy str): name of state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="delete")

    else:
        name: ""

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City
            instances equal to current State.id
            """
            from models import storage
            cities_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
