from email.mime.text import MIMEText

EMAIL = None
PASSPHRASE = None
HOST = None
PORT = None
FROM = EMAIL
SUBJECT = None
TO = None
BODY = None
CC = None
BCC = None
NAME = None
DATE = None
EXPIRES = None

BODY = MIMEText(BODY, 'HTML', 'UTF-8')
