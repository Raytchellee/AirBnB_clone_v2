#!/usr/bin/python3
"""This file contains tests for db_storage class"""

import unittest
from models.city import City
from models.state import State
from models.user import User
from models.engine.db_storage import DBStorage
from os import getenv


db = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(db != 'db', "Testing DBstorage only")
class test_DBStorage(unittest.TestCase):
    """Tests for DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Initialize the DBStorage and create tables"""
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """Close the session after all tests are done"""
        cls.storage.close()

    def test_new(self):
        """Test adding new objects to the database"""
        user1 = User(email="test@gmail.com", password="password")
        self.storage.new(user1)
        self.assertIn(user1, self.storage.all(User).values())

    def test_save(self):
        """Test saving changes to the database"""
        new_city = City(name="Aladin", state_id="34527")
        self.storage.new(new_city)
        self.storage.save()
        self.assertIn(new_city, self.storage.all(City).values())

    def test_delete(self):
        """Test deletng objects from the database"""
        new_state = State(name="Chicago")
        self.storage.new(new_state)
        self.storage.save()
        self.assertIn(new_state, self.storage.all(State).values())
        self.storage.delete(new_state)
        self.assertNotIn(new_state, self.storage.all(State).values())

    def test_all(self):
        """Test retrieving all objects from the database"""
        all_cities = self.storage.all(City)
        self.assertTrue(isinstance(all_cities, dict))

    def test_reload(self):
        """Test reloading the database"""
        old_user = User(email="test@gmail.com", password="password")
        self.storage.new(old_user)
        self.storage.save()
        self.assertIn(old_user, self.storage.all(User).values())
        self.storage.reload()
        self.assertNotIn(old_user, self.storage.all(User).values())


if __name__ == '__main__':
    unittest.main()
