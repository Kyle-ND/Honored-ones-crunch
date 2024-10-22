#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment 

def user_details():
    name = input("Enter name:")
    number = input("Enter number:")
    contact[name] = number
    print("contact added.")

def display_contact():
    print("contact:")
    for name, number in contact():
        print(f"{name}:{number}")