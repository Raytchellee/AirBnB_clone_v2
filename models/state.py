#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class State(BaseModel, Base):
    """ class called State """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete-orphan",
                          single_parent=True)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ returns cities in the state """
            from models import storage
            c_list = []
            for c in list(models.storage.all(City).values()):
                if self.id == c.state_id:
                    c_list.append(c)
            return c_list
