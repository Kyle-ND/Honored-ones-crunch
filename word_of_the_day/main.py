import smtplib
import random


def main():
    to_address = send_email("To: ")
    lines = get_qoute()
    send_mail(lines,to_address)


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
        # Assigns a number, in this range to rand_index
        random_quote = file_reader[rand_index]
        # Like saying random_quote = file_reader[2]
        print(random_quote)
        return random_quote






def send_email(message):
    """
    TODO
    write a function that sends
    an email to your self using 
    smtplib and return 'success ' or 'fail' if sending email failed
    """
    return input(message).strip()




def send_mail(message,send_to):
    admin_email = "onasihle123@gmail.com"
    password = "qorrigumncekigba"
    try:
    # starting server and connecting to gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(admin_email,password)

            server.sendmail(from_addr=admin_email,to_addrs=send_to,msg=f"subject: Word of the Day!\n\n{message}")

        print("email sent :)") 
    except SMTPServerDisconnected:
        print("Error while sending email ") 
        print("connection lost :(")  


if __name__ == "__main__":
    main()
    