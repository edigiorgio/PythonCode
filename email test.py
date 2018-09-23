import smtplib

sender = 'shellyrivera22@gmail.com'
receivers = ['edigiorgio88@hotmail.com']

message = """From: From Person <shellyrivera22@gmail.com>
To: To Person <edigiorgio88@hotmail.com>
Subject: SMTP e-mail test

test email"""

try:
    smtpObj = smtplib.SMTP('m.hotmail.com', 443)
    smtpObj.sendmail(sender, receivers, message)
    print("Succesffuly sent email")
except SMTPException:
    print("That didn't work")
