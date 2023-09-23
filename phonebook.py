import model.contact as contact

class Phonebook:

    def __init__(self):
        self.contacts = [contact.Contact]
        print("Starting phonebook application...")

    """
    Method for searching contacts using given fields
    """
    def search_contacts(self):
        print("Fields: \n 0. First Name \n 1. Last Name \n 2. Phone Number \n 3. Email Address")
        user_input = input("Please enter by which field you want to search contact: ")

        
    """
    Method for creating new contact
    """
    def create_contact(self):
        print("Creating contact...")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")

        email_address = input("Enter email address, press enter to skip: ")
        if email_address=="": email_address=None
        
        address = input("Enter address, press enter to skip: ")
        if address=="": address=None

        contact_exists=False

        for contact in self.contacts:
            if contact.get_first_name==first_name and contact.get_last_name==last_name:
                contact_exists=True
        
        if contact_exists==True:
            print("Contact already exists! Please check the contact details and delete or update it as per your need.")

        else:
            new_contact = contact.Contact(first_name,last_name,phone_number,email_address,address)
            self.contacts.append(new_contact)
            print("Contact added successfully!")


    """
    Method for updating existing contact if its present in the contact list
    """
    def update_contact(self):
        first_name = input("Enter first name of contact to be deleted: ")
        last_name = input("Enter last name of contact to be deleted: ")

        for contact in self.contacts:
            if contact.get_first_name==first_name and contact.get_last_name==last_name:
                break

        print("Fields: \n 0. First Name \n 1. Last Name \n 2. Phone Number \n 3. Email Address \n 4. Address")
        user_input = input("Enter which field you want to update: ")
        if user_input=="0":
            updated_first_name=input("Enter the new first name: ")
            self.contacts

    def delete_contact(self):
        pass