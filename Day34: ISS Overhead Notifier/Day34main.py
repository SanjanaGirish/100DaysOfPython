import requests
from datetime import datetime
import smtplib

# 404 response code : resource doesn't exist
# 1xx: Hold on
# 2xx: Here you go
# 3xx: Don't have permission to get this
# 4xx: You screwed up the api code
# 5xx: The server screwed up (server / website is down)
MY_LAT = 25.55
MY_LONG = 25.55
my_email = "* ENTER YOUR GMAIL HERE *"
password = "* ENTER YOUR GMAIL PASSWORD HERE *"

def is_overhead():
    """ Function to see if ISS is +-5 degrees overhead"""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    return ((iss_lat in range(round(MY_LAT+5), round(MY_LAT-5)))
            and (iss_lng in range(round(MY_LONG+5), round(MY_LONG-5))))


def is_night():
    parameters = {"lat":MY_LAT, "lng": MY_LONG}
    response = requests.get(url="https://api.sunrise-sunset.org/json",
                        params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data['results']['sunrise'].split('T')[1].split(":")[0])
    sunset_hour = int(data['results']['sunset'].split('T')[1].split(":")[0])
    current_hour = datetime.now().hour
    return current_hour >= sunset_hour or current_hour <= sunrise_hour

if is_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Look Up \n\n"
                                f"The ISS is above you in the sky")
