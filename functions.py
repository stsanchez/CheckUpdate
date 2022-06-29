from email import message
from email.mime.text import MIMEText
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
import smtplib

#FUNCTION TO SEND AN EMAIL WITH THE INFORMATION OBTAINED AS PARAMETER

def sendMail(name_file):
    msg = MIMEMultipart()
    message = "The last file is " + name_file
    server = smtplib.SMTP('smtp.office365.com' ,587)
    msg['From'] = "myemail@domain.gob.ar"
    password = "password"
    msg['To'] = "toemail@domain.gob.ar"
    msg['Subject'] = "Alert"
    msg.attach(MIMEText(message, 'plain'))
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    