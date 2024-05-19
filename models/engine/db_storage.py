#!/usr/bin/python3
"""SQLAlchemy engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Handles db storage using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes an instance of DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries db depending on classname """
        objects = {}
        classes = [City, State, User, Place, Review]

        if cls:
            classes = [cls]

        for _ in classes:
            objs = self.__session.query(_).all()
            for obj in objs:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """ Adds the object to the current db session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes to the current db session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from current db session if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables & current db session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        self.__session = scoped_session(session_factory)

    def close(self):
        """call remove() method on the private session attribute
        (self.__session) or close() on the class Session
        """
        self.__session.remove()
