import requests
from datetime import datetime
import smtplib as st
import time

MY_EMAIL = "maddalimgvk2003@gmail.com"
MY_PASSWORD = "Mgvk/2003"
MY_LAT = 12.825888
MY_LONG = 80.039520

def is_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()


    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <=  iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

def send_mail():
    time.sleep(60)
    while True:
        if is_near() and is_night():
            connection = st.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user= MY_EMAIL, password= MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: Look Up\n\n The ISS is above you hurry up!!")
            

