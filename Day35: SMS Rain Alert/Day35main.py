import requests
from twilio.rest import Client

api_key = "* ENTER DATA HERE *"
MY_LAT = 23.369900
MY_LONG = 85.325279
account_sid = "* ENTER DATA HERE *"
auth_token = "* ENTER DATA HERE *"


parameters = {"lat": MY_LAT,
              "lon": MY_LONG,
              "exclude": "current,minutely,daily",
              "appid": api_key}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params=parameters, verify=False)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hourly_data in weather_slice:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It will rain. Message sending.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. "
                     "Remember to bring an Umbrella ☂️",
                from_='* ENTER TRIAL NUMBER *',
                to='* ENTER YOUR NUMBER HERE *'
    )
    print(message.status)
