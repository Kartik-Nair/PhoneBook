# PhoneBook

The Phonebook Application is a Python program that allows users to manage their contacts effectively. 
With this application, users can add, update, delete, and search for contacts, as well as perform other useful operations.

## Features

- **Contact Management:** Create, update, delete, and view contacts.
- **Search:** Search for contacts by name, phone number, or email address.
- **Sorting:** Sort contacts in ascending or descending order by first name.
- **Grouping:** Group contacts alphabetically by the initial letter of their last names.
- **Contact History:** Keep track of contact creation and updates.
- **Batch Loading:** Add contacts in bulk from a CSV file.


## Classes

- **main.py** 

    - Main function to manage a phonebook application.

    - This function creates a phonebook object and presents a menu to the user to perform various operations.
    - The user can select an option by entering the corresponding number. 
    - The chosen operation is executed, and the user is prompted for further input until they choose to exit the program.

- **phonebook.py**

    - The Phonebook class allows users to create, update, delete, search, and perform various operations on contacts.

    - Attributes:
        - contacts (list): A list of Contact objects representing the phonebook's contacts.

    - Methods:
        - search_contacts(): Searches for contacts based on user-defined criteria.
        - create_contact(): Creates a new contact and adds it to the phonebook.
        - validate_phone_number(phone_number): Validates a phone number's format.
        - validate_email_address(email_address): Validates an email address's format.
        - update_contact(): Updates an existing contact's information.
        - delete_contact(): Deletes an existing contact from the phonebook.
        - print_all_contacts(): Prints details of all contacts in the phonebook.
        - print_contact_history(): Prints the contact history for a specific contact.
        - sort_contacts(): Sorts the contacts in the phonebook.
        - group_contacts(): Groups contacts by the initial letter of their last names.

- **contacts.py**

    - Represents a contact with personal information.

    - Attributes:
       - first_name (str): The first name of the contact.
       - last_name (str): The last name of the contact.
       - phone_number (str): The phone number of the contact.
       - email_address (str): The email address of the contact.
       - address (str): The address of the contact.
       - create_time (datetime): The timestamp when the contact was created.
       - update_time (datetime): The timestamp of the last update to the contact.
       - contact_history (list): A list of log entries documenting updates to the contact.
