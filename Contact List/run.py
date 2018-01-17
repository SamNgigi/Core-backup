#!/usr/bin/env python3.6
# Above code allows us to execute our file without having to type python out before running our script
# print("Testin testing");

from contact import Contact

# Creating a new contact


def create_contact(fname, lname, phone, email):
    """
    Function to create a new contact_list
    """
    new_contact = Contact(fname, lname, phone, email)
    return new_contact

# Save contacts


def save_contacts(contact):
    """
    Function to save contact
    """
    contact.save_contact()


# Delete contact


def del_contact(contact):
    """
    Function to delete a contact
    """
    contact.delete_contact()


# Finding a contact


def find_contact(number):
    """
    Function that finds a contact by number and returns the contract
    """
    return Contact.find_by_number(number)

# Check if a contract exists


def check_existing_contact(number):
    """
    Function that checks if a contact exists with that number and return Boolean
    """
    return Contact.contact_exist(number)

# Displaying all contacts


def display_contacts():
    """
    Function that returns all the save contacts
    """
    return Contact.display_contacts()

# Copy pasting


def copy_email(number):
    """
    Function that copys to machines clipboard
    """
    return Contacts.copy_email()


def main():
    print("Hello Welcome to your contact list. Whats your name?")
    user_name = input()
    print("")

    print(f"Hi {user_name}! What would you like to do?")
    print("")

    while True:
        print("""Use these short codes:
              nc - create new contact,
              dc- display contacts,
              fc - find a contact,
              ex - exit contact list.""")
        short_code = input().lower()
        print("_" * 20)
        if short_code == "nc":
            print("New Contact")
            print("_" * 20)

            print("Enter first name -")
            f_name = input()

            print("Enter last name -")
            l_name = input()

            print("Phone number -")
            p_number = input()

            print("Email address -")
            e_address = input()

            save_contacts(create_contact(f_name, l_name, p_number, e_address))

            print("")
            print(f"""New contact - {f_name} {l_name} """)
            print("")

        elif short_code == "dc":
            if display_contacts():
                print("Here is a list of all you contacts")
                print("")
                for contact in display_contacts():
                    print(
                        f"{contact.first_name} {contact.last_name} {contact.phone_number} {contact.email}")
                    print("")
            else:
                print("")
                print("You dont seem to have any contacts save yet")
                print("")

        elif short_code == "fc":
            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contact(search_number):
                search_contact = find_contact(search_number)
                print("_" * 20)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print("_" * 20)
                print(f"Phone number - {search_contact.phone_number}")
                print(f"Email address - {search_contact.email}")
                print("")
            else:
                print("That contact does not exist")
                print("")

        elif short_code == "ex":
            print("Bye! Seeya! Chow! Adious! Baadaye!")
            print("")
            break
        else:
            print("I really didn't get that. Please use the short codes below")
            print("")


if __name__ == '__main__':
    main()
