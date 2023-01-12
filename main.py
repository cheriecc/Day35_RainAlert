import os
import requests
from twilio.rest import Client

MY_LAT = 51.48    # 23.15
MY_LON = -3.18    # 113.33
API_KEY = os.environ.get("OWM_API_KEY") # "e9cfebd3ce453f2711ceafb84e7aa8c2"
EXCLUDE = "current,minutely,daily"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_ENDPOINT1 = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "AC149964b7b04f2cd0bc04a86a5e262509"
auth_token = os.environ.get("AUTH_TOKEN") # "69e063af4fdabccfe511482cb7b6d78a"

account_sid1 = "SKe84293bb592bd4f67fc3769489fb0372"
secret = "ose1j5Stljws6Gq9xvawJk25t7QSIvQc"
auth_token1 = "48d1b2ca97fcb501dfed4b342efb45b2"

parameter = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
}

response = requests.get(url=OWM_ENDPOINT, params=parameter)
response.raise_for_status()
data = response.json()
recent_weather_data = data["list"][:12]
# print(recent_weather_data)

will_rain = False
for item in recent_weather_data:
    condition_code = item["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        # pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, remember to bring your 🌂",
        from_="+12232107045",
        to="+447536146465"
    )
    print("Umbrella")
    print(message.status)