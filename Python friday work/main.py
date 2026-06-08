import requests


def get_weather(city):
    """
    Fetch weather data for a given city.

    Args:
        city (str): Name of the city

    Returns:
        dict: Weather information
    """

    # Free weather API endpoint
    url = f"https://wttr.in/{city}?format=j1"

    # Send GET request to API
    response = requests.get(url)

    # Convert response to JSON format
    data = response.json()

    # Extract useful information
    current = data["current_condition"][0]

    return {
        "city": city,
        "temperature": current["temp_C"],
        "humidity": current["humidity"],
        "condition": current["weatherDesc"][0]["value"]
    }


# Main program
if __name__ == "__main__":

    # Niger State capital
    city_name = "Minna"

    # Call function
    weather = get_weather(city_name)

    # Display result
    print("\n===== WEATHER APPLICATION =====")
    print(f"City: {weather['city']}, Niger State")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Condition: {weather['condition']}")
    print("================================")