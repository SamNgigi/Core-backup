class Contact:
    """
    Class that generates new instances of contacts
    """

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
