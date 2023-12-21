import time
import requests
import datetime as dt
import smtplib
LOCAL_UTC_OFFSET = 6
my_lat = 28.237988
my_lng = 83.995590
parameters={
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}
now = dt.datetime.now()
curr_time = now.hour


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour

def is_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (iss_latitude > my_lat-5 and iss_latitude < my_lat+5) and (iss_longitude > my_lng-5 and iss_longitude < my_lng+5):
        return True

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = utc_to_local(int(data["results"]["sunrise"].split("T")[1].split(":")[0]))
    sunset = utc_to_local(int(data["results"]["sunset"].split("T")[1].split(":")[0]))
    if curr_time > sunrise and curr_time < sunset:
        return True

while True:
    time.sleep(6000)
    if is_over_head() and is_night():
        my_email = "pythontest3967@gmail.com"
        my_password = "ruevmynqbbpslzkk"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)
            connection.sendmail(from_addr=my_email,to_addrs="dxngrg2058@gmail.com",msg="Subject: ISS \n\n Look above")