import requests
city = input("Enter a city name to get weather details: ")
print(f"{city} weather condition right now")
url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
response = requests.get(url)
data = response.json()
# print(url)
# print(response.text)
# print(response.status_code)
# print(type(data))
# print(data["results"][0]['latitude'])
# print(data["results"][0]['longitude'])
# print(data["results"][0])
# print(data["results"][1])
print("city:", data['results'][0]['name'])
print("latitude:", data['results'][0]['latitude'])
print("longitude:", data['results'][0]['longitude'])
print("country:", data['results'][0]['country'])
url2 = "https://api.open-meteo.com/v1/forecast"
params = {
    'latitude': data['results'][0]['latitude'],
    'longitude': data['results'][0]['longitude'],
    'current': "temperature_2m,weather_code,wind_speed_10m"
}
response2 = requests.get(url2, params=params)
# print(params)
# print(response2.status_code)
# print(response2.text)
weather_data = response2.json()
print("temperature: ")
print(weather_data['current']['temperature_2m'])
print("wind speed:")
print(weather_data['current']['wind_speed_10m'])
print("weather code with meanings are in documentation please refer to that at https://open-meteo.com/en/docs ")
print(weather_data['current']['weather_code'])
