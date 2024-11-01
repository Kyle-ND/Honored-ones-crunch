import smtplib
from random import choice

def get_qoute():
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
    filename = 'qoutes.txt'
    with open(filename,'r') as file_object:
        content = file_object.read()
    content = content.split('\n')
    ouput = choice(content)
    return ouput
#print(get_qoute())


def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """
    smtp_server = 'smtp.gmail.com'
    port = 587

    sender_email = 'tshepomajoro001@gmail.com'
    sender_email_password = '1@Thisguy'
    receiver_email = 'mothofeelama@gmail.com'

    email_subject = 'Testing'
    email_body = message
    complete_email = f"Subject: {email_subject}\n\n{email_body}"

    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls()
            server.login(sender_email,sender_email_password)
            server.sendmail(sender_email,receiver_email,complete_email)
            return 'success'
    except:
        return 'fail'

def main():
    """
    TODO
    write logic to use the two functions here
    """
    message = get_qoute()
    print(send_email(message))

main()