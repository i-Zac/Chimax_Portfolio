from flask import Flask, render_template, request, redirect, url_for
import csv
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import re

load_dotenv()
app = Flask(__name__)

# Configure email from .env
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/')
def home ():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/thank_you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return render_template('thank_you.html', name=name)

# saving submit to database csv
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])
# to validate email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# receiving form in my email function
def send_email(data):
    try:
        msg = Message(subject=f"New Contact Form Submission: {data['subject']}",
                      recipients=[os.getenv("MAIL_USERNAME")])
        # Plain text fallback
        msg.body = f"""
        Name: {data['name']}
        Email: {data['email']}
        Subject: {data['subject']}
        Message:
        {data['message']}
        """
        # Process message text to replace newlines with < br > BEFORE the f-string
        formatted_message = data['message'].replace('\n', '<br>')

        # --- NEW: HTML email content ---
        msg.html = f"""
        <html>
          <body>
            <h2 style="color:#4a148c;">New Contact Form Submission</h2>
            <p><strong>Name:</strong> {data['name']}</p>
            <p><strong>Email:</strong> {data['email']}</p>
            <h3><strong>Subject:</strong> {data['subject']}</h3>
            <p><strong>Message:</strong><br>{formatted_message}</p>
        </body>
        </html>
        """  # <--- This entire block is new and replaces plain formatting with HTML

        mail.send(msg)
    except Exception as e:
        print(f"Email sending failed: {e}")
        raise e  # or handle gracefully

def send_auto_reply(data):
    user_email = data['email']
    user_name = data['name']

    msg = Message(
        subject="Thanks for contacting me!",
        recipients=[user_email]
    )
    # Process message text to replace newlines with < br > BEFORE the f-string
    formatted_message1 = data['message'].replace('\n', '<br>')
    msg.html = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.5;">
        <h2 style="color:#444;">Hi {user_name},</h2>
        <p>Thank you for reaching out! I’ve received your message and will get back to you within 24 hours. <br> Looking forward to assisting you!</p>

        <p><strong>Here’s a copy of what you submitted:</strong></p>
        <div style="border-left: 3px solid #ccc; padding-left: 10px; color: #555;">
          <p><strong>Name:</strong> {data['name']}</p>
          <p><strong>Email:</strong> {data['email']}</p>
          <h3><strong>Subject:</strong> {data['subject']}</h3>
          <p><strong>Message:</strong><br>{formatted_message1}</p>
        </div>

        <p>Warm regards,<br>Adinnu Blessing Chiamaka <br>Virtual Assistant</p>
      </body>
    </html>
    """
    mail.send(msg)

# submitting contact form
@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            name = data.get("name", "Guest")
            email = data.get("email")
            subject = data.get("subject")
            message = data.get("message")
            if not is_valid_email(email):
                error_message = "Please enter a valid email address."
                return render_template('contact.html', error=error_message)

            # Save to CSV
            write_to_csv(data)

            # Send Email
            send_email(data)

            # Send auto-reply to user
            send_auto_reply(data)

            return redirect(url_for('thank_you', name=name))
        except Exception as e:
            print(f"Email error: {str(e)}")  # Logs error to the server console
            error_message = "Oops! Something went wrong while submitting your message. Please try again later."
            return render_template('contact.html', error=error_message)
    else:
        return 'Something went wrong! Try again!'

if __name__ == '__main__':
    app.run (debug = True)