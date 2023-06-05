import requests
import sys

API_KEY = "999fd252b84f56de3fd76ae7acc71d04"  

def fetch_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")
        sys.exit(1)
    except ValueError:
        print("Unable to parse weather data. Please try again.")
        sys.exit(1)

def parse_weather(weather_data):
    try:
        main_info = weather_data["weather"][0]["main"]
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]

        print(f"Weather: {main_info} ({description})")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    except (KeyError, IndexError):
        print("Unable to retrieve weather information. Please try again.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather_forecast.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    weather_data = fetch_weather(city)
    parse_weather(weather_data)

if __name__ == "__main__":
    main()