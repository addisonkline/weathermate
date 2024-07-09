import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv
import datetime

def send_email_process(subject, body, to_email, from_email, from_email_password, smtp_server, smtp_port):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login Credentials for sending the mail
    server.login(from_email, from_email_password)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())

    # Disconnect from the server
    server.quit()

def send_email(forecast: str):
    dotenv.load_dotenv()

    today = datetime.date.today()

    subject = f"Weather Summary for {today.month}/{today.day}/{today.year}"
    body = f"""Good morning {os.getenv('NAME')},
    
    Here is your daily weather summary:

    {forecast}

    Sincerely,
    Weathermate"""
    to_email = os.getenv('TO_EMAIL')
    from_email = os.getenv('FROM_EMAIL')
    from_email_password = os.getenv('FROM_EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER') 
    smtp_port = 587 

    send_email_process(subject, body, to_email, from_email, from_email_password, smtp_server, smtp_port)
