#!/usr/bin/python3
"""A unit test module for the console (command interpreter).
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.base_model import BaseModel
from models.user import User
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """"""
    @classmethod
    def setUpClass(cls):
        """"""
        cls.console = HBNBCommand()

    def setUp(self):
        """"""
        self.obj = BaseModel()
        self.user = User()

    def tearDown(self):
        """"""
        del self.obj
        del self.user

    def test_create(self):
        """"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(len(output), 36)  # Check if it's a valid UUID

    def test_show(self):
        """"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel {}".format(self.obj.id))
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.obj), output)

    def test_destroy(self):
        """ """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel {}".format(self.obj.id))
            output = mock_stdout.getvalue().strip()
            self.assertFalse(os.path.exists("file.json"))  # Check if object is deleted

    def test_all(self):
        """ """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.obj), output)
            self.assertIn(str(self.user), output)

    def test_update(self):
        """ """
        with patch('sys.stdout', new_callable=StringIO):
            self.console.onecmd("update BaseModel {} name 'New Name'".format(self.obj.id))
            self.assertEqual(self.obj.name, 'New Name')


if __name__ == '__main__':
    unittest.main()
