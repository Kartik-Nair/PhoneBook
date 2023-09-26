from model.contact import Contact
from datetime import datetime
import re

import csv

class Phonebook:

    """
    The Phonebook class allows users to create, update, delete, search, and perform various operations on contacts.

    Attributes:
        contacts (list): A list of Contact objects representing the phonebook's contacts.

    Methods:
        search_contacts(): Searches for contacts based on user-defined criteria.
        create_contact(): Creates a new contact and adds it to the phonebook.
        validate_phone_number(phone_number): Validates a phone number's format.
        validate_email_address(email_address): Validates an email address's format.
        update_contact(): Updates an existing contact's information.
        delete_contact(): Deletes an existing contact from the phonebook.
        print_all_contacts(): Prints details of all contacts in the phonebook.
        print_contact_history(): Prints the contact history for a specific contact.
        sort_contacts(): Sorts the contacts in the phonebook.
        group_contacts(): Groups contacts by the initial letter of their last names.
    """

    def __init__(self):
        self.contacts = [Contact]*0
        print("Starting phonebook application...")
        
    def search_contacts(self):

        """
        Searches for contacts in the contact list based on user-defined criteria.

        The method allows the user to choose between two search options:
        - 0: Search by name or phone number. The user can enter characters and view matching results.
        - 1: Search for contacts added within a specific time frame. The user enters start and end dates.

        Depending on the user's choice, the method displays matching results or contacts 
        added within the specified time frame.

        Returns:
            None
        """
        
        choice = input("Options: \n 0. Search with name or phone number \n " + 
                       "1. Search for contacts added within specific time frame \n How do you want to search for the contact: ")
        
        if choice == "0":
            user_input = input("To search for contacts, start entering characters below and press enter to see results: \n")
            counter = 0

            print("Below is a list of matching results: \n")
            for contact in self.contacts:
                if (user_input in contact.get_first_name() 
                    or user_input in contact.get_last_name() 
                    or user_input in contact.get_phone_number() 
                    or user_input in contact.get_email_address() 
                    or user_input in contact.get_address()):

                    print("Contact id: ", counter)
                    contact.print_contact()
                    counter+=1
                    print("\n \n")

        elif choice == "1":
            start_date = input("Please enter start date in yyyy/MM/dd format: ")
            end_date = input("Please enter end date in yyyy/MM/dd format: ")
            while True:

                try:
                    start_time=datetime(*[int(i) for i in start_date.split('/')])
                    end_time=datetime(*[int(i) for i in end_date.split('/')]).replace(hour=23,minute=59,second=59)
                    break
                except:
                    print("Please enter a valid date")
            print("Start time: ", start_time)
            print("End Time: ", end_time)
            filtered_contacts = [filtered_contact for filtered_contact in self.contacts if start_time <= filtered_contact.create_time <= end_time]
            
            print("\nBelow is a list of matching results: \n")
            counter = 0

            for contact in filtered_contacts:
                print("Contact id: ", counter)
                contact.print_contact()
                counter+=1
                print("\n \n")

        else:
            print("Please enter a valid option")

    def create_contact(self):

        """
        Creates a new contact and adds it to the contact list.

        This method provides two options to create a contact:
        - Option 0: Manually enter individual contact details 
        - Option 1: Load contacts in batch from a CSV file.

        Depending on the user's choice, the method either guides the user to enter 
        individual contact details or loads contacts from a CSV file. 
        It validates the phone number and email address format, checks for duplicate
        contacts, and adds the new contacts to the contact list.

        Returns:
            None
        """

        print("Creating contact...")

        print("Options: \n 0. Enter individual contact manually \n 1. Load contacts in batch from csv file")

        batch_load = input("How do you want to add contact: ")

        if batch_load=="0":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            while True:
                phone_number = input("Enter phone number in (XXX) XXX-XXXX format : ")

                if self.validate_phone_number(phone_number)==False:
                    print("Please enter a valid phone number. Make sure format is (XXX) XXX-XXXX") 
                    continue
                else:
                    break
            
            while True:
                email_address = input("Enter email address, press enter to skip: ")
                if email_address=="": email_address=None

           
                if self.validate_email_address(email_address)==False:
                    print("Please enter a valid email address.") 
                    continue
                else:
                    break
            
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
        
        elif batch_load=="1":
            print("We have sample_contacts.csv file already present in data folder. You can copy your required csv file to that path first.")
            file_name = input("Now enter the file name you want to load from the data folder:")
            csv_file_path = "data/"+file_name
            try:
                with open(csv_file_path, mode='r', newline='') as file:
                    csv_reader = csv.reader(file)

                    for contact in csv_reader:

                        first_name = contact[0]
                        last_name = contact[1]

                        phone_number = contact[2]
                        if self.validate_phone_number(phone_number)==False:
                            print("Phone number: ", phone_number, " is not valid format (XXX) XXX-XXXX, exiting csv file. Please try again after fixing the value in csv file.") 
                            return
                        
                        email_address = contact[3]
                        if email_address!="" and self.validate_email_address(email_address)==False:
                            print("Email address: ", email_address, " is not valid format, exiting csv file. Please try again after fixing the value in csv file.") 
                            return

                        address = contact[4]

                        contact_exists=False

                        for contact in self.contacts:
                            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                                contact_exists=True
                        
                        if contact_exists==True:
                            print("Contact with first name: ", first_name, " and last name: ", last_name + 
                                " already exists! Please check the contact details and delete or update it as per your need.")

                        else:
                            new_contact = Contact(first_name,last_name,phone_number,email_address,address)
                            self.contacts.append(new_contact)

                    print("Contacts added successfully from csv file in batch")
                    self.print_all_contacts()
            except:
                print("Error opening the file, please check the file name.")

        else:
            print("Please enter a valid option!")

    def validate_phone_number(self, phone_number):
        
        """
        Validates a phone number to ensure it matches the format '(###) ###-####'.

        Args:
            phone_number (str): The phone number to be validated.

        Returns:
            bool: True if the phone number is in the correct format, False otherwise.
        """

        pattern = r'^\(\d{3}\) \d{3}-\d{4}$'

        if re.match(pattern,phone_number):
            return True
        else:
            return False

    def validate_email_address(self, email_address):

        """
        Validates an email address to ensure it matches a standard email format.

        Args:
            email_address (str): The email address to be validated.

        Returns:
            bool: True if the email address is in a valid format, False otherwise.
        """
         
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email_address):
            return True
        else:
            return False

    def update_contact(self):

        """
        Updates an existing contact's information in the contact list.

        This method prompts the user to enter the first name and last name of the contact to be updated.
        If the contact is found, the user is presented with a menu to choose which field to update:
        - 0: First Name
        - 1: Last Name
        - 2: Phone Number
        - 3: Email Address
        - 4: Address

        After selecting a field to update, the user is prompted to enter the new value for that field.
        The contact's information is then updated, and the updated contact list is displayed.

        If the specified contact does not exist in the list, a message is displayed indicating that
        the contact was not found.
        """

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

    def delete_contact(self):

        """
        Deletes an existing contact from the contact list.

        This method prompts the user to enter the first name and last name of the contact to be deleted.
        If the contact is found in the list, it is removed from the list, and a confirmation message
        is displayed indicating that the contact has been deleted.

        If the specified contact does not exist in the list, a message is displayed indicating that
        the contact was not found.

        Returns:
            None
        """

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

    def print_all_contacts(self):

        """
        Prints the details of all contacts in the contact list.

        This method displays the details of each contact in the contact list using a counter 
        to keep track of contact ids displayed. 
        If the contact list is empty, it notifies the user to add new contacts.

        Returns:
            None
        """

        counter = 0
        if(self.contacts.count==0):
            print("Contact list is empty, please add new contacts.")
        else:
            print("\nFull Contact List: ")
            for contact in self.contacts:
                print("Contact id: ", counter)
                contact.print_contact()
                counter+=1
                print("\n \n")

    def print_contact_history(self):

        """
        Prints the contact history for a specific contact.

        This method prompts the user to enter the first name and last name of a contact 
        to retrieve their contact history.
        If the contact is found in the contact list, it displays their contact history, 
        which may include details of previous interactions or communications.

        If the specified contact does not exist in the list, a message is displayed indicating 
        that the contact was not found.

        Returns:
            None
        """
        
        first_name = input("Enter first name of contact: ")
        last_name = input("Enter last name of contact: ")
        found_contact=False
        for contact in self.contacts:
            if contact.get_first_name()==first_name and contact.get_last_name()==last_name:
                found_contact=True
                print("Contact History: ", contact.get_contact_history())

        if found_contact==False:
                print("Contact does not exist, please check the first and last name you entered.")

    def sort_contacts(self):

        """
        Sorts the contacts in the contact list based on the user's choice.

        This method allows the user to choose between two sorting options:
        - 0: Ascending order based on first names.
        - 1: Descending order based on first names.

        Depending on the user's choice, it sorts the contacts accordingly and provides feedback 
        to the user.

        Returns:
            None
        """
    
        choice=input("\n\nOptions: \n0. Ascending order \n1. Descending order \n\nHow do you want to sort: ")
        
        if choice=="0":
            self.contacts.sort(key=lambda contact: contact.get_first_name())
            print("Contacts sorted in ascending order. Press 4 to view all contacts.")
        elif choice=="1":
            self.contacts.sort(key=lambda contact: contact.get_first_name(), reverse=True)
            print("Contacts sorted in descending order. Press 4 to view all contacts.")
        else:
            print("Please enter a valid option")

    def group_contacts(self):

        """
        This method sorts the contacts based on the initial letter of their last names, 
        effectively grouping them alphabetically. 

        Returns:
            None
        """
        
        print("Grouping contacts by initial letter of last name")
        self.contacts.sort(key=lambda contact:contact.get_last_name()[0] )
        print("Contacts successfully grouped. Press 4 to view all contacts.")
