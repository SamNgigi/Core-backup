# unitest is the module with all the properties and methods that allow for testing
import unittest
# Importing that class Contact
from contact import Contact
# We download this third party module below using python3.6 -m pip install pyperclip
import pyperclip

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
  # Just like the setUp() method the tearDown() method executes a set of instructions after every test

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """

        # Here the tearDown() method assigns the contact_list in the Contact class empty. This helps us get accurate test results everytime have a new test case
        Contact.contact_list = []
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

    # Second test
    # We want to test if we can save contacts.
    # indentation wise it below function has to be on the same line with the ohter functions
    def test_save_contact(self):
        """
        test_save_contact test case to test if the contact object is saved into the contact list
        """
        # .save_contact() is the save to contact function.
        # Test would check if an addition has been made to our contact list
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    # Test to se if we can add to contact list multiple times
    def test_save_multiple_contact(self):
        """
        def test_save_multiple_contact to check if we can save multiple contacts to our contact_list
        """
        self.new_contact.save_contact()
        # new contact
        test_contact = Contact("Test", "user", "0798765432", "test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    # Test to see if we can delete contacts
    def test_delete_contact(self):
        """
        test_delete_contact to test if we can remove a contact from our contact list
        """
        self.new_contact.save_contact()
        # new contact
        test_contact = Contact("Test", "user", "0745639300", "test@usr.com")
        # new contact saved
        test_contact.save_contact()
    #    For deleting the new contact
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list), 1)

    # Test to see if we can search and find our saved contacts
    def test_find_by_number(self):
        """
        Test to check if we can find a contact by phone nuber and display any information.
        """
        self.new_contact.save_contact()
        # new contact
        test_contact = Contact("Test", "user", "0748363839", "test@user.com")
        test_contact.save_contact()
        # The number that we find in found_contact should be the same as the one in test_contact for the test to pass.
        # If they aren't the same...the test will always fail
        found_contact = Contact.find_by_number("0748363839")
        # The test
        self.assertEqual(found_contact.email, test_contact.email)
    # Test to see if a contact exists

    def test_contact_exists(self):
        """
        Test to check if we can return a Boolean if we cannot find the contact.
        """

        self.new_contact.save_contact()
        # Test user
        test_contact = Contact("Test", "user", "0722334455", "test@user.com")
        # We save
        test_contact.save_contact()
        # variable that stores what we expect
        contact_exists = Contact.contact_exist("0722334455")
        # The test that should return a variable
        self.assertTrue(contact_exists)

    def test_display_all_contact(self):
        """
        Method that returns a list of all contacts saved.
        """
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

   # We want to test if we can copy paste info.
    def test_copy_email(self):
        """
        Test to confirm that we are copying the email address from a found contact
        """
        self.new_contact.save_contact()
        Contact.copy_email("0712345678")
        self.assertEqual(self.new_contact.email, pyperclip.paste())


        # Below we are simply stating that if the module being tested is running we collect the test methods and execute them.
if __name__ == "__main__":
    unittest.main()
