
import RPi.GPIO as GPIO
import time
import sys
import os


FB_LOCK[4] = {6,13,19,26};

GPIO.setmode(GPIO.BCM)
GPIO.setup(FB_LOCK[0],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(FB_LOCK[1],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(FB_LOCK[2],GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(FB_LOCK[3],GPIO.IN,pull_up_down=GPIO.PUD_UP)  
 

GPIO.setwarnings(False)  
try:
	while True:
		if GPIO.input(FB_LOCK[0]):
			print("LOCK 1 feedback received")
		elif GPIO.input(FB_LOCK[1]):
			print("LOCK 2 feedback received")
		elif GPIO.input(FB_LOCK[2]):
			print("LOCK 3 feedback received")
		elif GPIO.input(FB_LOCK[3]):
			print("LOCK 4 feedback received")
   
except KeyboardInterrupt:  
    
finally:  
    GPIO.cleanup() # this ensures a clean exit  