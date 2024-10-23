#use python dictionaries to create a function that prompts a user to enter their name and number and 
#display what the contact book looks like at the moment 

def contact_book():
  contact_book_dict = {}
  n = 5
  
  name = input("Enter name:\n")
  number = int(input("Enter number:\n"))
  contact_book_dict[name] = number
  
  while n > 5:
      contact_book() 
      n -= 1
 
  print(contact_book_dict)
  

contact_book()
    
# Copy pasted MY CODE, had forgotten to fork this