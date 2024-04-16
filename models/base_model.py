#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Datetime, String

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models

    Attrs:
        id (sqlachemy str): BaseModel id
        created_at (sqlalchemy datetime): time of creation
        updated_at (sqlalchmey datetime): time of update
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            
            # Converts str rep of datetime to an obj
            
            for attr_name in ['created_at', 'updated_at']:
                if attr_name in kwargs:
                    setattr(self, attr_name, datetime.strptime(kwargs[attr_name],
                                                                '%Y-%m-%dT%H:%M:%S.%f')
            # Remove '__class__' key from kwargs
            kwargs.pop('__class__', None)

            # Update instance attrs from kwargs

            for key, val in kwargs.items():
                setattr(self, key, val)
    

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new()
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # Remove sa_instance_state if it exists

        dictionary.pop('_sa_instance_state', None)

        return dictionary


    def delete(self):
        """Deletes current instance from the storage"""
        models.storage.delete(self)
