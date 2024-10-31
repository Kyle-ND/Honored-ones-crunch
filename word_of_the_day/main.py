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
    admin_email = "scelonkululeko2@gmail.com"
    send_to ="scelonkululeko2@gmail.com"
    password = "what ever man!"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as sever:
            sever.starttls()
            sever.login(admin_email, password)

            sever.sendmail(from_addr=admin_email, to_addrs=send_to, msg=f"subject: word of the day!\n\n{message}")
        print("email sent :")
    except smtplib.SMTPServerDisconnected:
        print("Error while sending email")
        print("Connection lost : )")

def main():
    """
    TODO
    write logic to use the two functions here
    """
    return send_email(get_qoute())
if __name__ == '__main__':
    main()