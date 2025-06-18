import requests
from datetime import datetime
import smtplib
import time

My_latitude = 30.229290
My_longitude = -93.217110
My_email = "iamakashpatel1@gmail.com"
My_password = "zmnm yutn ilnb mufr"

def is_overhead():
    information = requests.get(url = "http://api.open-notify.org/iss-now.json")
    data = information.json()["iss_position"]
    longitude = float(data["longitude"])
    latitude = float(data["latitude"])

    if My_latitude - 5 <= latitude <= My_latitude+5 and My_longitude - 5 <= longitude <= My_longitude+5:
        return True


def is_night():
    parameters = {
        "lat":My_latitude,
        "lng":My_longitude,
        "formatted":0
    }
    respond = requests.get(" https://api.sunrise-sunset.org/json", params = parameters )
    data = respond.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time  = datetime.now().hour
    if time >= sunset or time <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=My_email,password=My_password)
        connection.sendmail(
            from_addr=My_email,
            to_addrs=My_email,
            msg="Subject: \n\n  The iss is above you in the sky"
        )








































