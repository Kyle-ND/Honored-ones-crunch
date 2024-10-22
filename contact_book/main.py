#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment
 
def Add_contacts():

    contact_book = {}

    name = input("Enter Name: ")
    number = input("Enter Number: ")

    contact_book[name] = number
    print(contact_book)

Add_contacts()

