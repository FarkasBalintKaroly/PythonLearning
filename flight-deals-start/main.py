# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Update excel sheet with iata codes
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        city_name = row["city"]
        row["iataCode"] = flight_search.get_destination_code(city_name)
    # print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    # data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

# Check for flights
for destination in data_manager.destination_data:
    flight = flight_search.check_flights(origin_city_code=ORIGIN_CITY_IATA,
                                         destination_city_code=destination["iataCode"],
                                         from_time=tomorrow,
                                         to_time=six_month_from_today)
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
