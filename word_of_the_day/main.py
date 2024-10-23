import smtplib

import random


"""
TODO
write a function that reads 'qoutes.txt'
and returns a randomly selected qoute from the 
qoutes.txt file.
"""
def choose_random_line(file_path): 
    with open(file_path, 'r') as file: 
        lines = file.readlines()  
    return random.choice(lines).strip()  

file_path = 'qoutes.txt'  
random_line = choose_random_line(file_path) 
print(random_line) 



"""
TODO
write a function that sends
an email to your self using 
smtplib and return 'success ' or 'fail' if sending email failed
"""
def send_email(message):
    s = smtplib.SMTP('madeupemail@gmail.com', 587)
    s.starttls()
    s.login("madeupemail@gmail.com", "Whateverthepasswordis30#")
    message = "Message you need to send"
    s.sendmail("madeupemail@gmail.com", message)
    s.quit()

    """
    TODO
    write logic to use the two functions here
    """

def main():
