import smtplib
import random

def get_qoute():
    """
    TODO
    write a function that reads 'qoutes.txt'
    and returns a randomly selected qoute from the 
    qoutes.txt file.
    """
    with open('word_of_the_day/qoutes.txt', 'r', errors='ignore') as f:
        qoutes = f.read()

    qoutes_lines = qoutes.splitlines()
    rand_qoute = random.randrange(0, len(qoutes_lines))
    return qoutes_lines[rand_qoute]

def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = 'scelonkululeko2@gmail.com'
    password = 'uhqx blcd qrve updl'
    mail.login(sender, password)

    recipient = 'bnnneffect2@gmail.com'
    subject = 'Email to my self'

    header = f'To: {recipient}\nFrom: {sender}\nSubject: {subject}\n'
    message = header + message

    mail.quit()

    if mail == "success":
        return "success"
    else:
        return "failed"

def main():
    """
    TODO
    write logic to use the two functions here
    """
    return send_email(get_qoute())
print(main())
