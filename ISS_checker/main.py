import requests
from datetime import datetime
import smtplib
import time


# See if ISS is above us
def is_above():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_longitude = float(data_iss["iss_position"]["longitude"])
    iss_latitude = float(data_iss["iss_position"]["latitude"])

    max_lat = MY_LAT + 5
    min_lat = MY_LAT - 5
    max_lng = MY_LONG + 5
    min_lng = MY_LONG - 5
    if (iss_longitude < max_lng) and (iss_longitude > min_lng) \
            and (iss_latitude < max_lat) and (iss_latitude > min_lat):
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    # Get sunset and sunrise times
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour < sunrise or hour > sunset:
        return True
    else:
        return False


MY_LAT = 47.188721
MY_LONG = 18.413811

my_email = MY_EMAIL
password = MY_PASSWORD
to_email = MY_EMAIL
message = "Subject:ISS is above you!!\n\nLook Up!"

while True:
    time.sleep(60)
    # if iss is above and is dark - do
    if is_above() and is_dark():
        # send an email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)
