import smtplib
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(receiver_email, otp):
    sender_email = "admin@mail.com"   # Replace with your Gmail email address
    sender_password = "***************" # Replace with your Gmail account password or App Password

    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        print("OTP sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


