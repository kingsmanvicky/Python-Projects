import datetime as dt
import pandas
import random
import smtplib as sp

MY_EMAIL = "maddalimgvk2003@gmail.com"
MY_PASSWORD = "rbhmlvfkfptgussf"f


today = (dt.datetime.now().month, dt.datetime.now().day)


data = pandas.read_csv("birthdays.csv")


birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows() }
if today in birthdays_dict:
    birthday_person = birthdays_dict[today] 
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with sp.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg= f"Subject:HAppy Birthday!!\n\n {contents}")


