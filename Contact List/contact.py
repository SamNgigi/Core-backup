import pyperclip


class Contact:
    """
    Class that generates new instances of contacts
    """
   # meant to be in the same indent with the function below
    contact_list = []

    def __init__(self, first_name, last_name, phone_number, email):
        """
        __init__ method that helps us define for our objects.

        i.e
          Args:
              first_name: New contact first name.
              last_name: New contact last name.
              number: New contact phone number.
              email: New contact  email address.

        The "self" python keyword can be likened to "this" in java & javascript
        """

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
   # Indentatation of this one has to be on same line with the above init function

    def save_contact(self):
        """
        save_contact method saves contact objects into contact_list
        """

        Contact.contact_list.append(self)

    def delete_contact(self):
        """
        delete_contact method delete a saved contact from the contact_list.
        """
        Contact.contact_list.remove(self)
# Below we have the decorator @classmethod. Decorators allow us to make simple modifications to callable objects like functions.
# This @classmethod simply informs the interpreter that this is a method that belongs to the entire class

    @classmethod
    def find_by_number(cls, number):
        """
        Method that takes in a number and returns a contact that matches that number.

        Args:
         number: Phone number to search for
        Returns:
         Contact of the person that matches the number.
        """

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls, number):
        """
        Method that checks if a contact exists from the contact list.
        Args:
         number:Phone number to search if it exists
        Returns:
          Boolean: True or flase depending if the contact exists
        """
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False

    @classmethod
    def display_contacts(cls):
        """
        Method that returns the contact list
        """
        return cls.contact_list

    @classmethod
    def copy_email(cls, number):
        # We get the email of the contact by first getting the contact object by using the fin_byNumber method. We then use the pyperclip.copy()and pass in the contact email address using contact_found.email
        contact_found = Contact.find_by_number(number)
        # We then use the pyperclip.copy() and pass in the contact email address.
        # Pyperclip.copy() method allows us to copy passed items to the machines clipboard
        pyperclip.copy(contact_found.email)
