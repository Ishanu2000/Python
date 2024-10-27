import json

#Represent an individual contact with name, phone, and email
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

#Manage the phonebook
class Phonebook:
    def __init__(self):
        self.contacts = {}  #Dictionary to store contacts with name as key

    #Add a contact to the phonebook
    def add_contact(self, contact):
        if contact.name in self.contacts:
            print(f"Contact '{contact.name}' already exists.")
        else:
            self.contacts[contact.name] = contact
            print(f"Contact '{contact.name}' added.")

    #Remove a contact from the phonebook
    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed.")
        else:
            print("Contact not found.")

    #Search for a contact by name
    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("Contact not found.")

    #Display all contacts in the phonebook
    def display_all_contacts(self):
        if not self.contacts:
            print("Phonebook is empty.")
        else:
            print("\n----- All Contacts -----")
            for contact in self.contacts.values():
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    #Save contacts to a text file
    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                #Saving contacts as JSON for easy loading and readability
                json.dump({name: vars(contact) for name, contact in self.contacts.items()}, file, indent=4)
            print(f"Contacts saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    #Load contacts from a text file
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = {name: Contact(**details) for name, details in data.items()}
            print(f"Contacts loaded from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading from file: {e}")

#Example
#Create a Phonebook instance
phonebook = Phonebook()

#Add contacts to the phonebook
phonebook.add_contact(Contact("Ishan", "071-1234567", "ishan@mail.com"))
phonebook.add_contact(Contact("Dinuka", "078-1237890", "dinuka@mail.com"))

#Display all contacts
phonebook.display_all_contacts()

#Search for a specific contact
phonebook.search_contact("Ishan")

#Remove a contact
phonebook.remove_contact("Dinuka")

#Display all contacts after removal
phonebook.display_all_contacts()

#Save contacts to a text file
phonebook.save_to_file("phonebook.txt")

#Load contacts from a text file
phonebook.load_from_file("phonebook.txt")

#Display all contacts after loading
phonebook.display_all_contacts()
