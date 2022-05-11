# import smtplib

# my_email = "* ENTER YOUR GMAIL HERE *"
# password = "* ENTER YOUR GMAIL PASSWORD HERE *"
# receiver_email = "* ENTER RECIPIENT YAHOO MAIL HERE *"

# # Way for us to connect to our email provider's smtp connector
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
# # Makes the connection secure
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=receiver_email,
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# The current time now
# import datetime as dt
# now = dt.datetime.now()
# print(now.year)
# print(now.month)
# print(now.hour)
# print(now.minute)
# print(now.weekday())

# if now.year == 2021:
#     print("Remember to wear a mask.")

# date_of_birth = dt.datetime(day=28, month=2, year=2021,
#                             hour=4, minute=1, second=20)
# print(date_of_birth)
