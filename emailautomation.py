import smtplib
import ssl
from email.message import EmailMessage

from blinker import receiver_connected

subject = "email from python"
body= "this is chandan automation"
sender_email = "chandan.d.sm.eng01@gmil.com"
receiver_email = "chandan.sm.eng01@gmail.com"
password = input("enetr password ;")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
     server.login(sender_email,password)
     server.sendmail(sender_email,receiver_email,message.as_string)
  
