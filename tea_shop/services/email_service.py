import smtplib



class EmailServices():
    def send_email(self, message, sender, recipient):
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("EMAIL_ID", "EMAIL_PASSWORD")
            message = "Hello "
            s.sendmail("EMAIL_ID", recipient, message)
            s.quit()
        except Exception as e:
            print(f"Error sending email: {e}")

