import psutil
import time
import smtplib
from email.mime.text import MIMEText

# Set up email details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_FROM = 'sylvestorsielei@gmail.com'
EMAIL_PASSWORD = '0710730535'
EMAIL_TO = 'silvestorsielei@gmail.com'

# Check if laptop is on
def is_laptop_on():
    battery = psutil.sensors_battery()
    if battery is not None:
        plugged = battery.power_plugged
        percent = battery.percent
        return plugged or percent > 5
    else:
        return True