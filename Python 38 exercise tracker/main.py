import requests
from datetime import datetime

APP_ID = "app_2ac90eb7e2fa4aab9811e0fc"
API_KEY = "nix_live_PUAyUm2lRkZuApg0XQmZh3E4TUPUEIEH"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_text = input("Tell me your exercises: ")

parameters = {
    "query": exercise_text
}

response = requests.post(
    url=exercise_endpoint,
    json=parameters,
    headers=headers
)

print("STATUS CODE:", response.status_code)
result = response.json()
print("RESPONSE:", result)

if response.status_code == 200 and "exercises" in result:

    now_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%H:%M:%S")

    with open("workouts.txt", "a") as file:
        for exercise in result["exercises"]:
            file.write(
                f"{now_date} | {now_time} | "
                f"{exercise['name'].title()} | "
                f"{exercise['duration_min']} min | "
                f"{exercise['nf_calories']} kcal\n"
            )

            print("Logged:", exercise["name"])

else:
    print("Something went wrong. Check API response above.")