import requests
from flight_data import FlightData
import os

TEQUILA_API_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_API_ENDPOINT}/locations/query"
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        iata_code = data["locations"][0]["code"]
        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_API_ENDPOINT}/v2/search", headers=headers, params=params)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(price=data["price"],
                                 departure_city=data["route"][0]["cityFrom"],
                                 departure_airport_code=data["route"][0]["flyFrom"],
                                 destination_city=data["route"][0]["cityTo"],
                                 fly_to=data["route"][0]["flyTo"],
                                 out_date=data["route"][1]["local_departure"].split("T")[0],
                                 return_date=data["route"][1]["local_departure"].split("T")[0])
        print(f"{flight_data.destination_city}: $ {flight_data.price}")
        return flight_data
