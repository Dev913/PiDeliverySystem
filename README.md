# PiDeliverySystem
A system that betters most delivery notification systems. System was written in python.

# Requirements
1. Raspberry Pi
2. Raspberry Pi Camera
3. Rasberry Pi Case With Power Button!
5. Email
6. Twilio Account with twilio phone number and regular phone number
7. Auxillary to USB Converter + Auxillary Cord + Auxillary Compatible Speaker

# How to utilize?
1. Flash rasbian onto your raspberry pi (Tutorial: https://www.raspberrypi.org/documentation/installation/installing-images/)
2. Follow Substeps

  Substep 1: Download files and extract the Data folder and PiDeliverySystem.py along with requirements.py to Desktop
  
  Substep 2: Open terminal and run "Cd Desktop"
  
  Substep 3: run "Python requirements.py"
  
  Substep 4: Type in "Crontab -e"
  
  Substep 5: Go to end of file and paste "@reboot sudo python /home/pi/Desktop/PiDeliverySystem.py"
  
  Substep 6: Press Ctrl + o to save
  
  Substep 7: Press Ctrl + x to exit
  
 3. You are setup! Now just explain to your Delivery Person how to use it and you will get notified on delivery!
