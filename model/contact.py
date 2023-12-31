from datetime import datetime

class Contact:

    """
    Represents a contact with personal information.

    Attributes:
        first_name (str): The first name of the contact.
        last_name (str): The last name of the contact.
        phone_number (str): The phone number of the contact.
        email_address (str): The email address of the contact.
        address (str): The address of the contact.
        create_time (datetime): The timestamp when the contact was created.
        update_time (datetime): The timestamp of the last update to the contact.
        contact_history (list): A list of log entries documenting updates to the contact.
    """

    create_time=0
    update_time=0
    

    def __init__(self, first_name, last_name, phone_number, email_address, address):

        """
        Initializes a new contact object.

        This constructor method initializes a new contact object with the provided information.
        It sets the contact's first name, last name, phone number, email address, and address.
        It also records the creation time and adds an entry to the contact's history log.

        Args:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
            phone_number (str): The phone number of the contact.
            email_address (str): The email address of the contact.
            address (str): The address of the contact.

        Returns:
            None
        """
        
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        self.create_time=datetime.now()
        self.update_time=datetime.now()
        self.contact_history=[]
        add_log=("Created new contact with Name: " + first_name + " " + last_name + ", Phone number: " + phone_number + 
                ", Email Address: " + email_address + ", Address: " + address + ", at time: " + str(self.create_time))
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

        """
        This method takes a new first name as input and updates the contact's first name.
        It also records the update time and adds an entry to the contact's history log.

        Args:
            first_name (str): The new first name for the contact.

        Returns:
            None
        """
        
        print("Updating first name to: " + first_name)
        self.first_name = first_name
        self.update_time=datetime.now()
        update_log=("Update contact with First Name: " + self.first_name + ", at time: " + str(self.update_time))
        self.contact_history.append(update_log)

    def update_last_name(self, last_name):

        """
        This method takes a new last name as input and updates the contact's last name.
        It also records the update time and adds an entry to the contact's history log.

        Args:
            last_name (str): The new last name for the contact.

        Returns:
            None
        """

        print("Updating last name to: " + last_name)
        self.last_name = last_name
        self.update_time=datetime.now()
        update_log=("Update contact with Last Name: " + self.last_name + ", at time: " + str(self.update_time))
        self.contact_history.append(update_log)

    def update_phone_number(self, phone_number):

        """
        This method takes a new phone number as input and updates the contact's phone number.
        It also records the update time and adds an entry to the contact's history log.

        Args:
            phone_number (str): The new phone number for the contact.

        Returns:
            None
        """

        print("Updating phone number to: " + phone_number)
        self.phone_number = phone_number
        self.update_time=datetime.now()
        update_log=("Update contact with Phone Number: " + self.phone_number + ", at time: " + str(self.update_time))
        self.contact_history.append(update_log)

    def update_email_address(self, email_address):

        """
        This method takes a new email address as input and updates the contact's email address.
        It also records the update time and adds an entry to the contact's history log.

        Args:
            email_address (str): The new email address for the contact.

        Returns:
            None
        """

        print("Updating email address to: " + email_address)
        self.email_address = email_address
        self.update_time=datetime.now()
        update_log=("Update contact with Email Address: " + self.email_address + ", at time: " + str(self.update_time))
        self.contact_history.append(update_log)

    def update_address(self, address):

        """
        This method takes a new address as input and updates the contact's address.
        It also records the update time and adds an entry to the contact's history log.

        Args:
            address (str): The new address for the contact.

        Returns:
            None
        """
          
        print("Updating address to: " + address)
        self.address = address
        self.update_time=datetime.now()
        update_log=("Update contact with Address: " + self.address + ", at time: " + str(self.update_time))
        self.contact_history.append(update_log)

    def print_contact(self):

        """
        Prints the details of the contact.

        Returns:
            None
        """

        print("First Name: ",self.get_first_name())
        print("Last Name: ",self.get_last_name())
        print("Phone Number: ",self.get_phone_number())
        print("Email Address: ",self.get_email_address())
        print("Address: ",self.get_address())
        print("Created on: ", self.create_time)
        print("Last updated on: ", self.update_time)
