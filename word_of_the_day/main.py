import smtplib

import random
def get_qoute(qoutes.txt):
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
with open(qoutes.txt, 'r') as file: 
	lines = file.readlines() 
	random_line = random.choice(lines) 
    return random_line 
    


def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """

def main():
    """
    TODO
    write logic to use the two functions here
    """