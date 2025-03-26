import smtplib

sendermail = 'xxxxxx@gmail.com'
senderpassword= 'xxxxx'
receviermail ='xxxxxxx'
subject = "xxxxxx"

s= smtplib.SMTP("smtp.gmail.com" ,587)
s.starttls()
s.login(sendermail,senderpassword)
s.sendmail(sendermail,receviermail,subject)
s.quit()
