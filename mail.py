import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage


bodyText = "This is just a test. This email is generated using Python. :)"
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('venuvardhanreddytekula8@gmail.com', '<pwd>')


def sendMail():
	msg = MIMEText(bodyText)
	print "1"
	msg['Subject'] = 'Attempt to send an email Using Python'
	print "2"
	msg['From'] = "venuvardhanreddytekula8@gmail.com"
	print "3"
	msg['Reply-To'] = "vinay.n.varma189@gmail.com "
	print "4"
	msg['To'] = "vinay.n.varma189@gmail.com"
	print "5"
	mail.sendmail('venuvardhanreddytekula8@gmail.com', 'vinay.n.varma189@gmail.com', msg.as_string())
	print "6"

try:
	sendMail()
except:
    print "Caught it!"
