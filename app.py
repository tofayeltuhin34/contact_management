# contact management system
from utils import database


def menu():

    user_choice = input("""
        Enter C - For create contact
        Enter S - For show all contact
        Enter E - For Edit a contact
        Enter D - For delete any contact
        Enter M - For add another(extra) number to the same person
        Enter a - For search a contact
        Enter Q  - to Exit 
        
    """)

    while user_choice != 'q':
        if user_choice == 'c':
            create_contact()
        elif user_choice == 's':
            show_contacts()
        elif user_choice == 'd':
            delete_contacts()
        elif user_choice == 'e':
            edit_contact()
        elif user_choice == 'm':
            edit_multiple_contact_number()
        elif user_choice == 'a':
            search_contact()
        else:
            print('wrong keyword - please try again..')

        user_choice = input("""
                Enter C - For create contact
                Enter S - For show all contact
                Enter E - For Edit a contact
                Enter D - For delete any contact
                Enter M - For add another(extra) number to the same person
                Enter a - For search a contact
                Enter Q  - to Exit 

        """)


def create_contact():
    database.create()


def show_contacts():
    contacts = database.show()
    for _ in contacts:
        print(f"Name: {_['name']}, Number:{_['number']}, Email:{_['email']}, Extra Number: {_['extra number']}")


def delete_contacts():
    name = input('Enter the name you want to delete: ')
    database.delete(name)


def edit_contact():
    name = input("Enter the contact name you want to edit: ")
    database.edit(name)


def edit_multiple_contact_number():

    name = input("Enter the contact name you want to edit: ")
    database.multiplecontact(name)


    name = input("Enter the contact name who have multiple number: ")
    database.multiple_number(name)



def search_contact():
    name = input('Enter search name:')
    database.search(name)


menu()
