import phonebook as pb

def main():

    """
    Main function to manage a phonebook application.

    This function creates a phonebook object and presents a menu to the user to perform various operations.
    The user can select an option by entering the corresponding number. 
    The chosen operation is executed, and the user is prompted for further input 
    until they choose to exit the program.
    """

    phonebook = pb.Phonebook()
    while True:
        
        print("\n\nMain Menu: \n 0. Search Contacts \n 1. Add Contacts \n" + 
              " 2. Update Contacts \n 3. Delete Contacts \n 4. View All Contacts \n 5. Print Contact History \n 6. Sort Contacts \n 7. Group contacts \n 8. Exit")
        user_input = input("Please enter your option here: ")

        if user_input == "0":
            phonebook.search_contacts()
        elif user_input == "1":
            phonebook.create_contact()
        elif user_input == "2":
            phonebook.update_contact()
        elif user_input == "3":
            phonebook.delete_contact()
        elif user_input == "4":
            phonebook.print_all_contacts()
        elif user_input == "5":
            phonebook.print_contact_history()
        elif user_input == "6":
            phonebook.sort_contacts()
        elif user_input == "7":
            phonebook.group_contacts()
        elif user_input == "8":
            break
        else:
            print("Please enter a valid option!")

if __name__=="__main__":
    main()
