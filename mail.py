import smtplib

sendermail = 'mohitgupta42284228@gmail.com'
senderpassword= 'ptffmuodxkpiwirg'
receviermail ='sagar.shakya561@gmail.com'
subject = "namaste"

s= smtplib.SMTP("smtp.gmail.com" ,587)
s.starttls()
s.login(sendermail,senderpassword)
s.sendmail(sendermail,receviermail,subject)
s.quit()
