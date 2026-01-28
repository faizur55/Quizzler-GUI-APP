import requests

parameters = {
    "amount": 15,
    "type": "boolean",
    "category":27,
    "difficulty":"hard",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
