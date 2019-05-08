import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage

class mail:
    #Credentials
    

    @staticmethod
    def send_mail(my_ip):
        body = "New IP: " + my_ip
        msg = MIMEMultipart()
        msg["To"] = "a.wellnitz@prointernet.de"
        msg["From"] = "moin@wellnitz-alex.de"
        msg["Subject"] = "IP has changed!"

        msgText = MIMEText('<b>%s</b><br><br>' % (body), 'html')
        msg.attach(msgText)   # Added, and edited the previous line
        mail.sendEmail(msg)

    @staticmethod
    def sendEmail(msg):
        emailRezi = smtplib.SMTP(mail.mail_server, mail.mail_server_port)
        emailRezi.ehlo()
        emailRezi.starttls()
        emailRezi.set_debuglevel(1)
        emailRezi.login(mail.mail_username, mail.mail_password)
        #emailRezi.sendmail(from_addr, to_addr, email_message)
        emailRezi.sendmail(mail.from_addr, mail.to_addr, msg.as_string())
        emailRezi.quit()
        