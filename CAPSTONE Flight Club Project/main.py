# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests
from pprint import pprint

response = requests.get("https://api.sheety.co/d78a84bb057cdba2d3da100fb0de03f5/flightDeals/prices")
sheet_data = response.json()["prices"]
pprint(sheet_data)

