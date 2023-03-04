import psutil
import time
import smtplib
from email.mime.text import MIMEText

# Set up email details
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_FROM = 'silvestorsielei@gmail.com'
EMAIL_PASSWORD = 'fhkezamuepedboym'
EMAIL_TO = 'sylvestorsielei@gmail.com'

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

    # Main loop
while True:
    if is_laptop_on():
        send_email('Take a break!', 'It has been two hours. Please take a 15-minute break.')
        time.sleep(100) # 15 minutes
        send_email('Resume work', 'Your break is over. Please resume work.')
    else:
        time.sleep(80) # 10 minutes