#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime,timedelta
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.destination_data
for data in sheet_data:
    if data["iataCode"] == "":
        data["iataCode"] = flight_search.find_Iata(data["city"])

curr_date = datetime.now()
date_after_6months = curr_date + timedelta(days=6*30)
for city in sheet_data:
    search_result = flight_search.search("LON",city["iataCode"],
                                         curr_date.strftime("%d/%m/%Y"),
                                         date_after_6months.strftime("%d/%m/%Y"))
    if search_result.price <= city["lowestPrice"]:
        print(f"Got it! from London to {search_result.destination}\n You go on {search_result.out_date}"
              f"and you get in on {search_result.in_date}")
# pprint(sheet_data)
# data_manager.update_sheet()
# pprint(sheet_data)