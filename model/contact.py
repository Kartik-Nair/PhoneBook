from datetime import datetime

class Contact:

    create_time=0
    update_time=0
    contact_history=[]

    def __init__(self, first_name, last_name, phone_number, email_address, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        self.create_time=datetime.now()
        self.update_time=datetime.now()
        add_log=("Created new contact with Name: " + first_name + " " + last_name + ", Phone number: " + phone_number + 
                ", Email Address: " + email_address + ", Address: " + address + ", at time: " + self.create_time)
        self.contact_history.append(add_log)

    def get_first_name(self):
        return str(self.first_name)
    
    def get_last_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number
    
    def get_email_address(self):
        return self.email_address
    
    def get_address(self):
        return self.address
    
    def get_contact_history(self):
        return self.contact_history

    def update_first_name(self, first_name):
        print("Updating first name to: " + first_name)
        self.first_name = first_name
        self.update_time=datetime.now()
        update_log=("Update contact with First Name: " + self.first_name + ", at time: " + self.update_time)
        self.contact_history.append(update_log)


    def update_last_name(self, last_name):
        print("Updating last name to: " + last_name)
        self.last_name = last_name
        self.update_time=datetime.now()
        update_log=("Update contact with Last Name: " + self.last_name + ", at time: " + self.update_time)
        self.contact_history.append(update_log)

    def update_phone_number(self, phone_number):
        print("Updating phone number to: " + phone_number)
        self.phone_number = phone_number
        self.update_time=datetime.now()
        update_log=("Update contact with Phone Number: " + self.phone_number + ", at time: " + self.update_time)
        self.contact_history.append(update_log)

    def update_email_address(self, email_address):
        print("Updating email address to: " + email_address)
        self.email_address = email_address
        self.update_time=datetime.now()
        update_log=("Update contact with Email Address: " + self.email_address + ", at time: " + self.update_time)
        self.contact_history.append(update_log)

    def update_address(self, address):
        print("Updating address to: " + address)
        self.address = address
        self.update_time=datetime.now()
        update_log=("Update contact with Address: " + self.address + ", at time: " + self.update_time)
        self.contact_history.append(update_log)

    def print_contact(self):
        print("First Name: ",self.get_first_name())
        print("Last Name: ",self.get_last_name())
        print("Phone Number: ",self.get_phone_number())
        print("Email Address: ",self.get_email_address())
        print("Address: ",self.get_address())
        print("Created on: ", self.create_time)
        print("Last updated on: ", self.update_time)