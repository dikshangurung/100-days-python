
import requests

parameter = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean",params=parameter)
response.raise_for_status()
question_data = response.json()["results"]
