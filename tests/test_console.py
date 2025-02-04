#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class contains testing documentation of the command interpreter"""
    def test_HBNBCommand_class_docstring(self):
        """This tests for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_console_module_docstring(self):
        """This tests for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")


if __name__ == '__main__':
    unittest.main()
