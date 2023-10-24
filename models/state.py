#!/usr/bin/python3
""" State Module for HBNB project """
import os
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
            city_list = []
            store = storage._FileStorage__objects
            for key, val in store.items():
                parts = key.split(".")
                if parts[0] == "City":
                    if val.to_dict()["state_id"] == self.id:
                        city_list.append(val)
            return city_list
