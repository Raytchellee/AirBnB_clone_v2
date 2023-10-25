#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""

import os
from sqlalchemy import (create_engine)
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


envr = os.getenv('HBNB_ENV')
db = os.getenv('HBNB_MYSQL_DB')
host = os.getenv('HBNB_MYSQL_HOST')
passwd = os.getenv('HBNB_MYSQL_PWD')
username = os.getenv('HBNB_MYSQL_USER')


class DBStorage:
    """ Depicting a database storage object"""

    __engine = None
    __session = None

    def __init__(self):
        """ DBStorage initialization """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(username, passwd,
                                                 host, db),
            pool_pre_ping=True)

        if envr == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ show all objects cls as dictionary """
        obj = {}
        items = {'City': City, 'User': User,
                  'Place': Place, 'State': State,
                  'Review': Review, 'Amenity': Amenity}

        if cls is None:
            for cls in items:
                item = items[cls]
                res = self.__session.query(item)
                for idx in res:
                    new_id = idx.__class__.__name__ + '.' + idx.id
                    obj[new_id] = idx

        else:
            if type(cls) is str:
                item = items[cls]
            else:
                item = cls
            res = self.__session.query(item)
            for idx in res:
                new_id = idx.__class__.__name__ + '.' + idx.id
                obj[new_id] = idx

        return obj

    def new(self, obj):
        """ includes new object to database """
        self.__session.add(obj)

    def save(self):
        """ saves all changes to database """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes existing object from database """
        self.__session.delete(obj)

    def reload(self):
        """ reloads all changes to database """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        sesh = scoped_session(factory)
        self.__session = sesh()

    def close(self):
        """ closes the session"""
        self.__session.close()
