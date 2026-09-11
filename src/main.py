import pandas as pd
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

DATA_FILE = "data/cars.csv"
SOLD_FILE = "data/sold_cars.csv"

SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

print("Configure your email credentials before running.")
