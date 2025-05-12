import os
import yagmail

def send_email(subject, contents):
    try:
        # Initialize yagmail with your credentials from .env
        yag = yagmail.SMTP(user=os.getenv('GMAIL_USER_EMAIL'), 
                          password=os.getenv('GMAIL_APP_PASSWORD'))  # Changed from 'gmail_app_password' to 'GMAIL_APP_PASSWORD'
        
        # Send the email
        yag.send(to=os.getenv('GMAIL_USER_EMAIL'),
                 subject=subject,
                 contents=contents)
        
        print("Email sent successfully")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False