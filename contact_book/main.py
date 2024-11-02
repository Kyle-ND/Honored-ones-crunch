#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment 

first_name= input("Enter your name: ").title()
number = input("Enter your number: ")


def contact_book(first_name,number):
    
    person = {'first' : first_name, 'number': number}
    return person

user_info = contact_book(first_name,number)
print(user_info)
    
    

