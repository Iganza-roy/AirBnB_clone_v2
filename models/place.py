#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                            ForeignKey('places.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                            primary_key=True),
                        Column('amenity_id', String(60),
                            ForeignKey('amenities.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                            primary_key=True))

class Place(BaseModel, Base):
    """ Defines A place with set attributes """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                backref="place_amenities",
                                viewonly=False)
                                

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Getter method that returns a list of review instances
            with place_id == current place.id
            """
            from models import storage
            from models.review import Review

            all_reviews = models.storage.all(Review)
            return [review for review in all_reviews.values()
                    if review.place_id == self.id]


        @property
        def amenities(self):
            """Getter method that returns a list of review instances
            with place_id == current place.id
            """
            from models import storage
            from models.amenity import Amenity

            all_amenities = models.storage.all(Amenity)
            return [amenity for amenity in all_amenities.values()
                    if amenity.place_id == self.id]

