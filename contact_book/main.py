#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment

def contact_book():
    contacts = {}

    while True:
        name = input("Enter your name: ").lower()
        number = int(input("Enter your number: "))

        contacts[name] = number

        for contact, num in contacts.items():
            print(f"{contact}: {num}")

contact_book()