import requests
from twilio.rest import Client

API_KEY = "6523433303804fc21b1d474fc0d53520"
# MY_LAT = 28.237988
# MY_LON = 83.995590
MY_LAT = 11.396670
MY_LON = 105.424430
account_sid = "ACbd1a7674b841d50c7bd67f2a6904a36e"
auth_token = "0eb3ae6a0569ad74ae6b07245161a083"
parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
data = response.json()
data_slice = data["list"][:6]
for hour in data_slice:
    condition_code = hour["weather"][0]["id"]
    if condition_code<700:
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Bring umbrella",
            from_='+18623755349',
            to='+977 981 9109573'
        )
