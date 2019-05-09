# PiDeliverySystem
A system that betters most delivery notification systems. System was written in python.
But is not faster than all see not all are slow. For the ones that are slow i bettered.
I hope to help the ones that are slow as well what i mean is maybe they can utilize this project.

# Requirements
1. Raspberry Pi
2. Raspberry Pi Camera (Utlized to take picture of your delivery!)
3. Rasberry Pi Case With Power Button!
5. Email
6. Twilio Account with twilio phone number and regular phone number (OPTIONAL)
7. Auxillary to USB Converter + Auxillary Cord + Auxillary Compatible Speaker (OPTIONAL)

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
 
# Not a competition
Yes i do know that. But see some people get upset over idiotic occurences!
