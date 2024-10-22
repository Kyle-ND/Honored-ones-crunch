import smtplib


def get_qoute():
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
    with open("qoutes.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        print("Word of the day,", line.rstrip())


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