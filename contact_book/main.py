#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment 

def contact():
    user_name = input("Enter your name>> ")
    user_num = input("Enter your number>> ")
    user_info = {"User Name": "",
                 "User Number": 0}
    
    user_info["User Name"] = user_name
    user_info["User Number"] = user_num

    return user_info

print(contact())