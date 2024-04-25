# import smtplib
#
# my_email = "balintkarolyfarkas@gmail.com"
# password = "twch wedt mvya zojs"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="balintfarkaskaroly@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my e-mail.")
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# if year == 2024:
#     print(day_of_week)
#
# date_of_birth = dt.datetime(year=1999, month=6, day=5, hour=8, minute=30)
# print(date_of_birth)

import random
import smtplib
import datetime as dt
import os

# Get random quote from txt
with open(file="quotes.txt", mode="r") as file:
    quotes_list = file.readlines()

# Get the day of the week
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    random_quote = random.choice(quotes_list)
    # Send it in e-mail
    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_EMAIL_PASSWORD")
    to_email = os.environ.get("TO_EMAIL")
    message = f"Subject:Monday Motivation\n\n{random_quote}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
