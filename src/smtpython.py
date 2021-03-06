from email.mime.text import MIMEText
import smtplib

BCC = None
BODY = None
CC = None
DATE = None
EMAIL = None
EXPIRES = None
FROM = EMAIL
HOST = None
NAME = None
PASSPHRASE = None
PORT = None
SUBJECT = None
TO = None

BODY = MIMEText(BODY, 'HTML', 'UTF-8')
MAIL = 'Bcc: {}\nCc: {}\nDate: {}\nExpires: {}\nFrom: {} <{}>\nSubject: {}\nTo: {}\n{}'.format(BCC, CC, DATE, EXPIRES, NAME, FROM, SUBJECT, TO, BODY)

with smtplib.SMTP(HOST, PORT) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL, PASSPHRASE)
    smtp.sendmail(FROM, TO, MAIL)
    smtp.quit()
