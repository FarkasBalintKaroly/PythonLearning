import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
phone_num = os.environ.get("PHONE_NUM")

LAT = 47.188721
LONG = 18.413811

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_id = weather_data["list"][0]["weather"][0]["id"]

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+18582424486',
        to=phone_num
    )
    print(message.status)
