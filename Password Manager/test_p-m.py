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

        self.new_profile = Passwords("CIA", "myowncreativepass", "17")

    def tearDown(self):
        """
        This tearDown function cleans up after every test case.

        For example in this case...what we want is to return our password_list
        array to default even after multiple saves.
        """
        Passwords.password_list = []

    def test_instance(self):
        """
        test_instance tests if a the object created in setUp is initialized/
        instanciated properly.
        """

        self.assertEqual(self.new_profile.account_name, "CIA")
        self.assertEqual(self.new_profile.account_password,
                         "myowncreativepass")
        self.assertEqual(self.new_profile.password_length,
                         "17")

    def test_save_profile(self):
        """
        Test Case to test if the contact object is saved.

        So here it seems like we save try save our profile using a function on
        p_manager that we  have not built.
        This is what causes our test to fail and will only work when we build
        it and then import the working one
        """
        self.new_profile.save_profile()
        self.assertEqual(len(Passwords.password_list), 1)

    def test_save_multiple_profiles(self):
        """
        Test to see if our function can save multiple contacts.
        """
        test_profile = Passwords("Twitter", "newtwitteruser", "14")
        """
        test_profile does not need "self". Its a local variable
        """
        test_profile.save_profile()
        self.new_profile.save_profile()
        self.assertEqual(len(Passwords.password_list), 2)

    def test_display_profile(self):
        """
        Method that displays the list of all the profiles saved
        """
        self.assertEqual(Passwords.display_profile(), Passwords.password_list)

        # def test_passGenerated(self):
        #     """
        #     We want to test if our password generator will work. Hp
        #     """


if __name__ == "__main__":
    unittest.main()
