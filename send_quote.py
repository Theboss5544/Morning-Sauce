import smtplib
import urllib.request
import json
import os
from email.mime.text import MIMEText

# Pulled securely from GitHub Secrets - never hardcoded
GMAIL = os.environ['GMAIL']
GMAIL_APP_PASSWORD = os.environ['GMAIL_APP_PASSWORD']
PHONE_SMS_EMAIL = os.environ['PHONE_SMS_EMAIL']

def get_quote():
    url = "https://zenquotes.io/api/random"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        quote = data[0]['q']
        return f'Dwayne, {quote}'

def send_text(quote):
    msg = MIMEText(quote)
    msg['From'] = GMAIL
    msg['To'] = PHONE_SMS_EMAIL
    msg['Subject'] = "Morning Motivation"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL, PHONE_SMS_EMAIL, msg.as_string())
        print("Quote sent successfully")

if __name__ == "__main__":
    quote = get_quote()
    print(f"Sending: {quote}")
    send_text(quote)
