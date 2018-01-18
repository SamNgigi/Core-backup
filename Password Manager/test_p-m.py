#!/usr/bin/env python3.6
import unittest
from p_manager import Passwords


class TestPasswords(unittest.TestCase):
    """
    We have created a subclass class that inherits methods and
    properties from unitest.Test cases...i.e we have passed in the parent class
    of unittest as a parameter of the TestPasswords class.
    """

    def setUp(self):
        """
        This setUp() method allows us to define instructions that will be
        executed before each test method.

        So below we are going to instruct our method to create a new instance
        of the Passwords class before each test method is declared.


        We then store it as an instance variable in the test class as:
        self.new_password
        """
        self.new_accountpass = Passwords("CIA", "myowncreativepass")

    def test_instance(self):
        """
        test_instance tests if a the object created in setUp is initialized/
        instanciated properly.
        """

        self.assertEqual(self.new_accountpass.account_name, "CIA")
        self.assertEqual(self.new_accountpass.account_password,
                         "myowncreativepass")


if __name__ == "__main__":
    unittest.main()
