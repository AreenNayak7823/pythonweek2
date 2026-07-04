contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    print("Phone:", contacts.get(name, "Not found"))

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name] = input("Enter new phone number: ")
        print("Contact updated!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")


while True:
    print("\n1. Add  2. Search  3. Update  4. Delete  5. Exit")
    choice = input("Enter choice: ")
    if choice == '1': add_contact()
    elif choice == '2': search_contact()
    elif choice == '3': update_contact()
    elif choice == '4': delete_contact()
    elif choice == '5': break
