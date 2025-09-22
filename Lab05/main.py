""" LAB #05
    09/17/2025
    Student 1: Thi, Truong
    Student 2: Udonna, Uchegbulam

    A program that allows the user to view, search, and modify a contact list made up of
contact objects. A contact has a name, phone number, address, city, and zip code. Contacts are
initially read in from the file ‘addresses.txt’ and then are written back to the file when the
program ends.
"""
import check_input
from contact import Contact

def read_file():
    """ Read a file, store each line in a Contact object, store all objects in a list,
        sort and return the list of objects.

        Args: N/A
        Returns: a list of Contact objects
    """
    contact = []
    try:
        with open("addresses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    info = line.split(",")
                    user = Contact(*info)
                    contact.append(user)
            contact.sort()
            return contact

    except FileNotFoundError:
        print("Error: The file 'addresses.txt' was not found.")
        return []

def write_file(contacts):
    """ Write all elements from 'contacts' list to a file. Each object is on one line.
        Args: list of Contact objects
        Returns: N/A
    """
    with open("addresses.txt", "w") as file:
        for user in contacts:
            file.write(repr(user) + "\n")

def get_menu_choice():
    """ Display the main menu to the user and then take in and return
        the user’s valid input.
        Args: N/A
        Returns: an integer
    """

    print("\nRolodex Menu:")
    print("""1. Display Contacts
2. Add Contact
3. Search Contacts
4. Modify Contact
5. Save and Quit""")
    choice = check_input.get_int_range("> ", 1, 5)
    return choice

def modify_contact(cont):
    while True:
        print("""
Modify Menu:
1. First name
2. Last name
3. Phone
4. Address
5. City
6. Zip
7. Save""")
        choice = check_input.get_int_range("> ", 1, 7)

        if choice == 1:
            cont.f_name = input("Enter first name: ")
        elif choice == 2:
            cont.l_name = input("Enter last name: ")
        elif choice == 3:
            cont.phone = input("Enter phone number: ")
        elif choice == 4:
            cont.address = input("Enter address: ")
        elif choice == 5:
            cont.city = input("Enter city: ")
        elif choice == 6:
            cont.zip = input("Enter zip code: ")
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    contacts = read_file()

    while True:
        choice = get_menu_choice()

        if choice == 1: # Display Contacts
            print(f"\nNumber of contacts: {len(contacts)}\n")
            for i in range(len(contacts)):
                print(f"{i + 1}.", end=" ")
                print(contacts[i])
                print()

        elif choice == 2:   # Add Contact
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            city = input("Enter city: ")
            zip_code = input("Enter zip code: ")
            new_contact = Contact(first_name, last_name, phone, address, city, zip_code)
            contacts.append(new_contact)
            contacts.sort()

        elif choice == 3:   # Search contacts
            print("Search:")
            print("1. Search by last name")
            print("2. Search by zip code")

            search_choice = check_input.get_int_range("> ", 1, 2)

            if search_choice == 1:  # Search by last name
                last_name = input("Enter last name: ").strip()

                found = False
                for cont in contacts:
                    if cont.l_name.lower() == last_name.lower(): # avoid case-sensitivity
                        print(cont)
                        print()
                        found = True
                if not found:
                    print("Contact not found.\n")
            
            else:   # Search by zip code
                zip_code = input("Enter zip code: ").strip()

                found = False
                for cont in contacts:
                    if cont.zip == zip_code:
                        print(cont)
                        print()
                        found = True
                if not found:
                    print("Contact not found\n")

        elif choice == 4:   # Modify contact
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            found = False
            for cont in contacts:
                # use lower() function # avoid case-sensitivity
                if cont.f_name.lower() == first_name.lower() and cont.l_name.lower() == last_name.lower():
                    print(cont)
                    modify_contact(cont)
                    contacts.sort()
                    found = True
                    break
            if not found:
                print("Contact not found.")

        else:   # Save and Quit
            write_file(contacts)
            print("Saving file...")
            print("Ending program")
            break

if __name__ == "__main__":
    main()