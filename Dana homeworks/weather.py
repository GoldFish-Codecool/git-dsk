#Weather Checker: Create a program that fetches and displays the current weather for a given city. (Requires: requests library and an API like OpenWeatherMap)

import requests

city = input("Please input city: ")

API_key = "7eec51b4908d6b7a164eb78b4cbca8bc"

weatherdata = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric"
).json()

weather_description = weatherdata['weather'][0]['description']
temperature = weatherdata['main']['temp']

print(f"Weather: {weather_description}")
print(f"Temperature: {temperature}°C")
