##################### Hard Starting Project #################################

import datetime as dt
import smtplib
import pandas
from random import randint

my_email = "* ENTER YOUR GMAIL HERE *"
password = "* ENTER YOUR GMAIL PASSWORD HERE *"
# 1. Update the birthdays.csv with your friends & family's details.
# Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# Create a tuple from today's month and day using datetime.
now = dt.datetime.now()
today = (now.month, now.day)
#Use pandas to read the birthdays.csv
data = pandas.read_csv('birthdays.csv')
birthday_dict = {(row.month, row.day): row
                 for (index, row) in data.iterrows()}

if today in birthday_dict:
    info = birthday_dict[today]
    receiver_email = info["email"]
    with open(f'letter_templates/letter_{randint(1, 3)}.txt', 'r') as bday_card:
        content = bday_card.read()
        final = content.replace('[NAME]', str(info["name"]))
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
                            msg=f"Subject:Happy Birthday\n\n{final}")


