#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    """Defines place"""
    __tablename__ = "places"
    name = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all,delete")
    amenity_ids = []
    _amenities = relationship('Amenity', viewonly=False,
                              secondary='place_amenity', back_populates="place_amenities")

    @property
    def reviews(self):
        """gets review"""
        from models import storage
        result = []
        get_all = storage.all(Review)
        for review in get_all.values():
            if review.place_id == self.id:
                result.append(review)
        return result

    @property
    def amenities(self):
        """gets amenities"""
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        """sets amenities"""
        if (getenv('HBNB_TYPE_STORAGE') != "db"):
            try:
                if (value.__class__.__name__ == "Amenity"):
                    self.amenity_ids.append(value.id)
            except Exception:
                pass
            from models import storage
            all_amnty = storage.all(Amenity)
            temp_amnty = []
            for item in all_amnty.values():
                if item.id in self.amenity_ids:
                    temp_amnty.append(item)
            self._amenities = temp_amnty
