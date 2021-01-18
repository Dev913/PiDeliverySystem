# PiDeliverySystem
It is a delivery notification system it will help with delivery notifications so maybe if the users gone or there and is maybe asleep they will get 3 notifications via sms or verbally or email. Or even if their awake but maybe their elderly and can’t hear well this could help with that too. The main purpose though is to make sure the user gets their delivery notifications on time not all services delivery notification systems will alert the user right then and there.

# Requirements
* Raspberry Pi
* Raspberry Pi Camera (to take a picture of your delivery)
* Rasberry Pi Case With Power Button!
* Email (optional)
* Twilio Account with twilio phone number and regular phone number (optional)
* Auxillary to USB Converter + Auxillary Cord + Auxillary Compatible Speaker (optional)

# How to use?
* Flash rasbian onto your raspberry pi (Tutorial: https://www.raspberrypi.org/documentation/installation/installing-images/)
* Enable picamera with commmand "sudo raspi-config" Interfacing Options > Pi Camera > Enable
* Follow Substeps

  Substep 1: Download files and extract the Data folder and PiDeliverySystem.py along with requirements.py to Desktop
  
  Substep 2: Open terminal and run "Cd Desktop"
  
  Substep 3: run "Python requirements.py"
  
  Substep 4: Type in "Crontab -e"
  
  Substep 5: Go to end of file and paste "@reboot sudo python /home/pi/Desktop/PiDeliverySystem.py"
  
  Substep 6: Press Ctrl + o to save
  
  Substep 7: Press Ctrl + x to exit
  
* You are setup! Now just explain to your Delivery Person how to use it and you will get notified on delivery!
