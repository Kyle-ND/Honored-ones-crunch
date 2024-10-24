import smtplib


def get_qoute(file_path):
    try:
        with open(file_path):
            quotes = file.readlines()

quotes = [quote.strip() for quote in quotes if quote.strip()]

if not quotes:
    return "No quotes found."

return random.choice(quotes)

except FileNotFoundError:
    return "The file was not found"

quote = get_qoute('qoutes.txt')
print(qoute)
    




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