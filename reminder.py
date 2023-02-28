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

# Send email
def send_email(subject, body):
    message = MIMEText(body)
    message['subject'] = subject
    message['to'] = EMAIL_TO
    message['from'] = EMAIL_FROM

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())
    server.close()