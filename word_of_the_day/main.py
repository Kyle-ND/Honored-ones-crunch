import smtplib


def get_qoute(quotes_txt):
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
with open(quotes_txt, 'r') as file:
        quotes = file.readlines()
        print(random.choice(quotes).strip())

def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """
    sender = "Khensaneo@icloud.com"
    receiver = "Khensaneo@icloud.com"
def main():
    """
    TODO
    write logic to use the two functions here
    """