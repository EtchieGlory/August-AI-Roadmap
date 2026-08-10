import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CONDITIONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm"
}


def get_coordinates(city):
	params = {
        "name": city,
        "count": 1
    }

	response = requests.get(
        GEOCODING_URL,
        params=params,
        timeout=10
    )

	response.raise_for_status()

	data = response.json()

	if "results" not in data:
		return None

	location = data["results"][0]

	return (
        location["latitude"],
        location["longitude"]
    )


def get_weather(latitude, longitude):
	params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    }

	response = requests.get(
        WEATHER_URL,
        params=params,
        timeout=10
    )

	response.raise_for_status()

	data = response.json()

	current = data["current"]

	temperature = current["temperature_2m"]
	weather_code = current["weather_code"]

	condition = WEATHER_CONDITIONS.get(
        weather_code,
        "Unknown"
    )

	return temperature, condition


def main():
	print("=" * 30)
	print("       WEATHER TOOL")
	print("=" * 30)

	city = input("Enter city: ").strip()

	try:
		coordinates = get_coordinates(city)

		if coordinates is None:
			print("❌ City not found.")
			return

		latitude, longitude = coordinates

		temperature, condition = get_weather(
            latitude,
            longitude
        )

		print(f"\n📍 City: {city}")
		print(f"🌡️ Temperature: {temperature}°C")
		print(f"🌤️ Condition: {condition}")

	except requests.RequestException as error:
		print(f"❌ API request failed: {error}")


if __name__ == "__main__":
	main()