import smtplib
import dataframe as df
from tabulate import tabulate

table = lambda df: tabulate(df, headers='keys', tablefmt='psql')




def send_mail(message):
    print("sending report.....")
    # Python code to illustrate Sending mail from
    # your Gmail account

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("pubgacc1517@gmail.com", "Ilovepython!")
    # sending the mail
    s.sendmail("pubgacc1517@gmail.com", "azimarva@gmail.com", str(message))

    # terminating the session
    s.quit()
