import requests

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {"query": "run 3 miles"}

r = requests.post(url, json=data, headers=headers)

print(r.status_code)
print(r.text)