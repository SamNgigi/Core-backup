# unitest is the module with all the properties and methods that allow for testing
import unittest
# Importing that class Contact
from contact import Contact

# We create a subclass that inherits from unittest.TestCase. A subclass is just a normal class that can inherit methods and variables from other classes in addition to its own.


class TestContact(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours

    Args:
       unittest.TestCase: TestCase class that helps in creating test cases

    We pass in the parent class as a parameter in the parenthesis
    """

    def setUp(self):
        """
        Set up method to run before each test path. This method is what we will test against.
        """
        # Below creating the new contact object to test.
        self.new_contact = Contact(
            "James", "Muriuki", "0712345678", "james@moringaschool.com")

    # self.new_contact is an instance of the Contact class.
    # We create method test_init to check if our objects are instantiated corectly.

    def test_init(self):
        """
        has to be called test_init. This is to test if the object is initialized properly.
        """
        # the self.assertEqual() checks fofr an expected result
        # We are checking if the name and description of our new object is what we actually put
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "james@moringaschool.com")


# Below we are simply stating that if the module being tested is running we collect the test methods and execute them.
if __name__ == "__main__":
    unittest.main()
