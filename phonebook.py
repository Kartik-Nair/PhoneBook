from model.contact import Contact

class Phonebook:

    def __init__(self):
        self.contacts = [Contact]*0
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
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                contact_exists=True
        
        if contact_exists==True:
            print("Contact already exists! Please check the contact details and delete or update it as per your need.")

        else:
            new_contact = Contact(first_name,last_name,phone_number,email_address,address)
            self.contacts.append(new_contact)
            print("Contact added successfully!")
            self.print_all_contacts()


    """
    Method for updating existing contact if its present in the contact list
    """
    def update_contact(self):
        first_name = input("Enter first name of contact to be updated: ")
        last_name = input("Enter last name of contact to be updated: ")
        found_contact=False
        for contact in self.contacts:
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                found_contact=True
                print("Fields: \n 0. First Name \n 1. Last Name \n 2. Phone Number \n 3. Email Address \n 4. Address")
                user_input = input("Enter which field you want to update: ")
                if user_input=="0":
                    updated_first_name=input("Enter the new first name: ")
                    contact.update_first_name(updated_first_name)
                elif user_input=="1":
                    updated_last_name=input("Enter the new last name: ")
                    contact.update_last_name(updated_last_name)
                elif user_input=="2":
                    updated_phone_number=input("Enter the new phone number: ")
                    contact.update_phone_number(updated_phone_number)
                elif user_input=="3":
                    updated_email_address=input("Enter the new email address: ")
                    contact.update_email_address(updated_email_address)
                elif user_input=="4":
                    updated_address=input("Enter the new address: ")
                    contact.update_address(updated_address)
                else:
                    print("Please enter a valid option!")
                self.print_all_contacts()
            
        if found_contact==False:
                print("Contact does not exist, please check the first and last name you entered.")

        
    """
    Method for deleting existing contact from the contact list
    """
    def delete_contact(self):
        first_name = input("Enter first name of contact to be deleted: ")
        last_name = input("Enter last name of contact to be deleted: ")
        found_contact=False

        for contact in self.contacts:
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                found_contact=True
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
            
        if found_contact==False:
                print("Contact does not exist, please check the first and last name you entered.")


    """
    Method to print all contacts currently in the contact list
    """
    def print_all_contacts(self):
        counter = 0
        if(self.contacts.count==0):
            print("Contact list is empty, please add new contacts.")
        else:
            print("\nFull Contact List: ")
            for contact in self.contacts:
                print("Contact id: ", counter)
                contact.print_contact()
                print("\n \n")