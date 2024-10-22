#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment 

def contact_book():
    contacts = {}

    while True:
        name = input("Enter the contact's name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        number = input(f"Enter {name}'s phone number: ")
        
        # Update the contacts dictionary
        contacts[name] = number
        
        # Display the current contact book
        print("\nCurrent Contact Book:")
        for contact, phone in contacts.items():
            print(f"{contact}: {phone}")
        print()  # Add a newline for better readability

# Call the function
contact_book()
