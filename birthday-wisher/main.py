import pandas
import random
import datetime as dt
import smtplib
import os

# Import data row by row
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# Save letter templates location in a list
template_locations = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# Variables for e-mailing
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_EMAIL_PASSWORD")

# Check if today matches a birthday in the birthdays.csv
# Get today date
now = dt.datetime.now()
current_month = now.month
current_day = now.day

for data_row in data_dict:
    if data_row["month"] == current_month and data_row["day"] == current_day:
        # Pick a random letter template
        template = random.choice(template_locations)
        with open(file=f"letter_templates/{template}", mode="r") as file:
            letter_to_modify = file.read()
            modified_letter = letter_to_modify.replace("[NAME]", data_row["name"])

        # Send the letter in e-mail
        message = f"Subject:Happy Birthday!\n\n{modified_letter}"
        to_email = data_row["email"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
