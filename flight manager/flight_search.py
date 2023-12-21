import requests
from flight_data import FlightData
from pprint import pprint
from datetime import datetime,timedelta
curr_date = datetime.now()
date_after_6months = curr_date + timedelta(days=6*30)
tequilla_api = "nww4fugFqFnB8NXhtj4u57ZudTbBntj0"
search_endpoint = "https://api.tequila.kiwi.com/v2/search"
location_endpoint = "https://api.tequila.kiwi.com/locations/query"
class FlightSearch:
    def __init__(self):
        self.ok =2

    def find_Iata(self,city):
        header = {
            "apikey": tequilla_api,
        }
        parameter = {
            "term": city
        }
        response_location = requests.get(url=location_endpoint,params=parameter,headers=header)
        return response_location.json()["locations"][0]["code"]
    def search(self,from_city,to_city,date_from,date_to):
        header = {
            "apikey": tequilla_api,
        }
        parameter = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        search_response = requests.get(url=search_endpoint,params=parameter,headers=header)
        try:
            data = search_response.json()["data"][0]
        except IndexError:
            print("No flight found buddy")
            return None
        flight_info = FlightData(data["price"],data["cityTo"],
                                 data["route"][0]["local_departure"].split("T")[0],
                                 data["route"][1]["local_departure"].split("T")[0])
        # pprint(data["route"][0]["local_departure"].split("T")[0])
        # return data
        # pprint(data)
        return flight_info
        # return search_response.json()
    #This class is responsible for talking to the Flight Search API.

# flight = FlightSearch()
# flight.search("LON","PAR",curr_date.strftime("%d/%m/%Y"),date_after_6months.strftime("%d/%m/%Y"))