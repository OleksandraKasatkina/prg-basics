from contact import Contact 

class Contact_List:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def display_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts available.")