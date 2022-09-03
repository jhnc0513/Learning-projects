import requests

API_KEYS = "<YOUR_API_KEYS>"
SHEETY_ENDPOINTS = "https://api.sheety.co/<YOUR ID>/flightDeals/prices"
sheety_header = {
    "Authorization": API_KEYS
}
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINTS, headers=sheety_header).json()
        self.destination_data = response["prices"]
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_response = requests.put(url=f"{SHEETY_ENDPOINTS}/{city['id']}",json=new_data,headers=sheety_header)
            print(update_response.text)





