from flask import Flask, render_template, request
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

load_dotenv()


def send_email(subject, message, toEmail):
    # Email Configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = os.getenv('EMAIL')
    smtp_password = os.getenv('EMAIL_PASSWORD')

    # Email Structure
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = toEmail
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connection to the SMTP Server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # login acc
    server.login(smtp_username, smtp_password)
    # Send Message
    server.sendmail(smtp_username, toEmail, msg.as_string())

    # Quit the server
    server.quit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email_route():
    subject = request.form.get('subject')
    message = request.form.get('message')
    to_email = request.form.get('to_email')

    send_email(subject, message, to_email)

    return render_template('index.html', message='Email sent successfully')


if __name__ == '__main__':
    app.run(debug=True)
