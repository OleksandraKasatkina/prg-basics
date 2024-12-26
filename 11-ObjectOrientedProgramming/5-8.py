from contact_list import Contact_List
from contact import Contact

def main():
    contact_list = Contact_List()

    john = Contact("John Brown", "brown@onet.pl", "555234000")
    anna = Contact("Anna May", "am@o2.pl", "232000199")
    george = Contact("George Small", "smallg@google.pl", "222999100")
    paola = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")
    
    # Add contacts to the contact list
    contact_list.add_contact(john)
    contact_list.add_contact(anna)
    contact_list.add_contact(george)
    contact_list.add_contact(paola)
    
    # Display the contact list
    contact_list.display_contacts()

if __name__ == "__main__":
    main()