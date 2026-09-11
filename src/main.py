import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

DATA_FILE = #Car data file path
SOLD_FILE = #Sold car data file path

SENDER_EMAIL = #Email Id
APP_PASSWORD = # App password

while True:

    df = pd.read_csv(DATA_FILE)

    budget = float(input("Budget: "))
    max_km = float(input("Max KM: "))
    model = input("Model: ").lower()

    min_price = budget * 0.95
    max_price = budget * 1.05

    cars = []

    for i in range(len(df)):

        row = df.iloc[i]

        if row["model"].lower() == model:

            if row["km"] <= max_km:

                if row["previous_owners"] == 1:
                    final_price = row["price"] * 0.95
                else:
                    final_price = row["price"] * 0.925

                if min_price <= final_price <= max_price:

                    cars.append([
                        row["ID"],
                        row["model"],
                        row["km"],
                        round(final_price,2)
                    ])

    if len(cars) == 0:
        print("No Cars Found")
        continue

    result = pd.DataFrame(
        cars,
        columns=["ID","Model","KM","Final Price"]
    )

    print(result)

    car_id = int(input("Enter Car ID: "))

    car = df[df["ID"] == car_id].iloc[0]

    if car["previous_owners"] == 1:
        final_price = car["price"] * 0.95
    else:
        final_price = car["price"] * 0.925

    customer_email = input("Customer Email: ")

    message = f"""
Congratulations!

You purchased a car.

Car ID : {car['ID']}
Model : {car['model']}
KM : {car['km']}
Owners : {car['previous_owners']}
Final Price : {round(final_price,2)}

Purchase Time :
{datetime.now()}
"""

    msg = MIMEText(message)

    msg["Subject"] = "Car Purchase Confirmation"
    msg["From"] = SENDER_EMAIL
    msg["To"] = customer_email

    try:

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        server.login(
            SENDER_EMAIL,
            APP_PASSWORD
        )

        server.send_message(msg)

        server.quit()

        print("Email Sent Successfully")

    except Exception as e:

        print("Email Error")
        print(e)

    sold = pd.DataFrame([{
        "Email": customer_email,
        "ID": car["ID"],
        "Model": car["model"],
        "KM": car["km"],
        "Final Price": round(final_price,2),
        "Time": datetime.now()
    }])

    try:
        old = pd.read_csv(SOLD_FILE)
        sold = pd.concat([old,sold])
    except:
        pass

    sold.to_csv(SOLD_FILE,index=False)

    df = df[df["ID"] != car_id]

    df.to_csv(DATA_FILE,index=False)

    print("Car Purchased Successfully")

    again = input("Search Again (yes/no): ")

    if again.lower() != "yes":
        break
