import smtplib
import yaml
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from picamera import PiCamera
import twilio
from twilio.rest import Client
from os import system

with open('/home/pi/Desktop/Data/data.yaml', 'r') as data:
    data = yaml.load(data, Loader=yaml.FullLoader)
host = data['host']
port = data['port']
email = data['email']
password = data['password']
account_sid = data['accountsid']
auth_token = data['authtoken']
to = data['to_phone_number']
twilio_generated_phone_number = data['twilio_generated_phone_number']

camera = PiCamera()
camera.capture('/home/pi/Desktop/delivery.png')
msg = MIMEMultipart()
msg['From']=email
msg['To']=email
msg['Subject']='You may have a delivery!'
img_data = open('/home/pi/Desktop/delivery.png', 'rb')
img = MIMEImage(img_data.read())
img_data.close()
img.add_header('Content-ID', '<{}>'.format('/home/pi/Desktop/delivery.png'))
msg.attach(img)
config = smtplib.SMTP(host, port)
config.starttls()
config.login(email, password)
config.sendmail(email, email, msg.as_string())
config.quit()

client = Client(account_sid, auth_token)
message = client.messages \
          .create(
              body="You may have a delivery!",
              from_=twilio_generated_phone_number,
              to=to
            )
system('google_speech -l en "You may have a delivery" -e repeat 10')