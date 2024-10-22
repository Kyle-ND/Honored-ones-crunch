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
    return input(message).strip()

from_address = send_email("From: ")
to_address = send_email("To: ")
print("Enter a message:\n")

email_lines = [f"From: {from_address}", f"To: {to_address}"]
print(email_lines)

while True:
    # EOFError occurs when python expects input but none is received
    try:
        line  = input()
    except EOFError:
        break
    else:
        email_lines = email_lines.append(line)

msg = "\r\n".join(email_lines)
print(f"Your message is {msg}. Message length is: {len(msg)}")

server = smtplib.SMTP("localhost")
server.set_debuglevel(1)
server.sendmail(from_address,to_address,msg)
server.quit()


def main():
    """
    TODO
    write logic to use the two functions here
    """