import smtplib
import random

def get_qoute():
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
    with open('word_of_the_day/qoutes.txt', 'r') as quotes_file:
        file_reader = quotes_file.readlines()

        rand_index = random.randrange(0,len(file_reader) -1)
        random_quote = file_reader[rand_index]
        print(random_quote)
        return random_quote
get_qoute()





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