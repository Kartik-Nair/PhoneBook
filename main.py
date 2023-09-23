import phonebook as pb

def main():
    phonebook = pb.Phonebook()
    while True:
        
        print("Main Menu: \n 0. Search Contact \n 1. Create Contact \n" + 
              " 2. Update Contact \n 3. Delete Contact \n 4. View All Contacts \n 5. Exit")
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
            break
        else:
            print("Please enter a valid option!")

if __name__=="__main__":
    main()
