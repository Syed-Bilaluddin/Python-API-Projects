from dotenv import load_dotenv
import os
import requests
load_dotenv()
API_KEY = os.getenv("API_KEY")
city = input("Enter your city: ")
parameters = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)

if response.status_code == 200:

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    speed = data["wind"]["speed"]
    condition = data["weather"][0]["main"]

    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Speed: {speed} km/h")
    print(f"Condition: {condition}")

elif response.status_code == 404:
    print("City not found")
elif response.status_code == 401:
    print("Invalid API key")
else:
    print("Something went wrong with the weather API.")



