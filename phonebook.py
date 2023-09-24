from model.contact import Contact
from datetime import datetime

import csv

class Phonebook:

    def __init__(self):
        self.contacts = [Contact]*0
        print("Starting phonebook application...")

    """
    Method for searching contacts using given fields
    """
    def search_contacts(self):
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
            start_time=datetime(*[int(i) for i in start_date.split('/')])
            end_time=datetime(*[int(i) for i in end_date.split('/')]).replace(hour=23,minute=59,second=59)
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

        
    """
    Method for creating new contact
    """
    def create_contact(self):
        print("Creating contact...")

        print("Options: \n 0. Enter individual contact manually \n 1. Load contacts in batch from csv file")

        batch_load = input("How do you want to add contact: ")

        if batch_load=="0":
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
        
        elif batch_load=="1":
            print("We have sample_contacts.csv file already present in data folder. You can copy your required csv file to that path first.")
            file_name = input("Now enter the file name you want to load from the data folder:")
            csv_file_path = "data/"+file_name

            with open(csv_file_path, mode='r', newline='') as file:
                csv_reader = csv.reader(file)

                for contact in csv_reader:

                    first_name = contact[0]
                    last_name = contact[1]
                    phone_number = contact[2]
                    email_address = contact[3]
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

        else:
            print("Please enter a valid option!")


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
                counter+=1
                print("\n \n")


    def print_contact_history(self):
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
        print("Grouping contacts by initial letter of last name")
        self.contacts.sort(key=lambda contact:contact.get_last_name()[0] )
        print("Contacts successfully grouped. Press 4 to view all contacts.")