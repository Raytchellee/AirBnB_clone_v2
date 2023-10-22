#!/usr/bin/python3
"""Module for DBStorage class"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm.session import Session
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

env = os.getenv('HBNB_ENV')
db = os.getenv('HBNB_MYSQL_DB')
host = os.getenv('HBNB_MYSQL_HOST')
user = os.getenv('HBNB_MYSQL_USER')
passwd = os.getenv('HBNB_MYSQL_PWD')


class DBStorage:
    """"Handles MySQL storage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Gets all objects or those specified in cls"""
        classes = {
                    'User': User, 'City': City,
                    'State': State,'Place': Place,
                    'Review': Review, 'Amenity': Amenity          
        }
        obj = {}
        if not cls:
            for elem in classes.values():
                for item in self.__session.query(elem):
                    idx = item.__class__.__name__ + '.' + item.id
                    obj[idx] = item
        else:
            for item in self.__session.query(cls):
                idx = item.__class__.__name__ + '.' + item.id
                obj[idx] = item
        return obj

    def delete(self, obj=None):
        """Deletes existing objects"""
        if obj:
            self.__session.delete(obj)

    def save(self):
        """Save a session"""
        self.__session.commit()

    def new(self, obj):
        """Includes new object"""
        self.__session.add(obj)

    def reload(self):
        """Reloads db"""
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Sesh = scoped_session(sesh)
        self.__session = Sesh()

    def close(self):
        self.__session.close()
