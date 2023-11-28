class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        matches = [contact for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone]
        if matches:
            print("\nSearch Results:")
            for match in matches:
                print(f"Name: {match.name}, Phone: {match.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact '{name}' updated successfully!")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            keyword = input("Enter search keyword (name or phone): ")
            contact_manager.search_contact(keyword)

        elif choice == "4":
            name = input("Enter contact name to update: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_manager.update_contact(name, new_phone, new_email, new_address)

        elif choice == "5":
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
