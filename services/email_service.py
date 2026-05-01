import smtplib
import os

class EmailServices():
    def send_email(self,subject, message, recipient):
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
            s.starttls()
            s.login( os.getenv("EMAIL_ID"), os.getenv("EMAIL_PASSWORD"))

            s.sendmail(os.getenv("EMAIL_ID"), recipient,subject,message)
            s.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

