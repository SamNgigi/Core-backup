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
