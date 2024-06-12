## Fork and Clone Tutorial

To contribute to this project, you need to fork and clone the repository. Follow these steps:

### Forking the Repository

1. **Navigate to the Repository:**
   Visit the GitHub page of the repository at [EmailSender](https://github.com/NightDev19/EmailSender).

2. **Fork the Repository:**
   In the top-right corner of the page, click the "Fork" button. This will create a copy of the repository in your GitHub account.

### Cloning the Repository

1. **Go to Your Forked Repository:**
   After forking, navigate to your GitHub profile and find the forked repository.

2. **Clone the Repository:**
   Click the green "Code" button, and then copy the URL provided (either HTTPS or SSH).

3. **Open Your Terminal:**
   Open a terminal on your local machine.

4. **Run the Clone Command:**
   Execute the following command in your terminal, replacing `<your-username>` with your GitHub username:

   ```bash
   git clone https://github.com/<your-username>/EmailSender.git
   ```

   Or, if using SSH:

   ```bash
   git clone git@github.com:<your-username>/EmailSender.git
   ```

### Navigating to the Project Directory

Once the repository is cloned, navigate to the project directory:

```bash
cd EmailSender
```

You now have a local copy of the repository and can begin working on the project!

## Setting Upstream Remote (Optional)

To keep your fork up-to-date with the original repository, you can set an upstream remote:

1. **Add Upstream Remote:**

```bash
git remote add upstream https://github.com/NightDev19/EmailSender.git
```

2. **Fetch Upstream Changes:**

```bash
  git fetch upstream
```

3. **Merge Upstream Changes into Local Branch:**

```bash
  git merge upstream/main
```

By following these steps, you can ensure your fork stays updated with the latest changes from the original repository.

## Using dotenv in Python with Flask

This tutorial will guide you through setting up environment variables using `dotenv` in your Flask application to send emails.

### Prerequisites

Make sure you have the following installed:

- Python
- Flask
- `python-dotenv` package

### Installation

1. **Install Flask and python-dotenv:**

   ```bash
   pip install Flask python-dotenv
   ```

## Setting Up Environment Variables

1.  **Create a .env file in the root directory of your project:**

    ```
    EMAIL=your_email@example.com
    EMAIL_PASSWORD=your_email_password
    ```

    Replace your_email@example.com and your_email_password with your actual email and password.

## Python Code

1. **Create a main.py file and add the following code:**

   ```
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

       # Login
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
   ```

## Running the Application

1. **Run the Flask application:**

   ```
   python main.py
   ```

   or

   ```
   flask --app main run --debug
   ```

2. **Navigate to http://127.0.0.1:5000/ in your web browser.** 3.**Use the form to send an email.**

Feel free to copy and paste this into your [Readme](README.md) file!
