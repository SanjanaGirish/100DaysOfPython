# Send an automated message on Monday with an inspirational quote

import datetime as dt
from random import choice
import smtplib

my_email = "* ENTER YOUR GMAIL HERE *"
password = "* ENTER YOUR GMAIL PASSWORD HERE *"
receiver_email = "* ENTER RECIPIENT YAHOO MAIL HERE *"

# Read from file
with open('quotes.txt', 'r') as file:
    content = file.read().splitlines()
quote_of_the_day = choice(content)

# Check current date
now = dt.datetime.now()
if now.weekday() == 1:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                            msg=f"Subject:Quote of the day\n\n"
                                f"{quote_of_the_day}")

