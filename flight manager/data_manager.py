import requests
from pprint import pprint
#pretty print hai guys

class DataManager:
    def __init__(self):
        self.sheet_link = "https://api.sheety.co/99febf72650bbd94b8342f71bd296feb/myFlights/prices"
        self.destination_data = requests.get(url=self.sheet_link).json()["prices"]
        # pprint(self.response_link.json())
        #This class is responsible for talking to the Google Sheet.
    def update_sheet(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response_update = requests.put(url=f"{self.sheet_link}/{row['id']}",json=new_data)
            print(response_update.text)
