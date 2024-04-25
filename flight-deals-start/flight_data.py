class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, departure_airport_code, departure_city, fly_to, destination_city, out_date, return_date):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.destination_airport = fly_to
        self.destination_city = destination_city
        self.out_date = out_date
        self.return_date = return_date
