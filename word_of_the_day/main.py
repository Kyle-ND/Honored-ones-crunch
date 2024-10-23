import smtplib
import random


"""
TODO
write a function that reads 'qoutes.txt'
and returns a randomly selected qoute from the 
qoutes.txt file.
"""
def choose_random_line(): 

    try:
        with open("word_of_the_day/qoutes.txt", 'r') as file: 
            lines = file.readlines()  
        return random.choice(lines).strip()  
    except FileNotFoundError:
        print("This file does not exist")




"""
TODO
write a function that sends
an email to your self using 
smtplib and return 'success ' or 'fail' if sending email failed
"""
def send_email(receiver_email):
    message = choose_random_line()
    s = smtplib.SMTP('madeupemail@gmail.com', 587)
    s.starttls()
    s.login("madeupemail@gmail.com", "Whateverthepasswordis30#")
    message = "Message you need to send"
    s.sendmail(receiver_email, message)
    return True
    
    """
    TODO
    write logic to use the two functions here
    """

def main():
    receiver_email = input("Enter email: ")
    if send_email(receiver_email):
        print("Email sent")
    

   

main()


