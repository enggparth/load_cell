# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
lock = 14
led = 15


# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(lock, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
#GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(lock, GPIO.LOW)
GPIO.output(led, GPIO.LOW)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.5)


except KeyboardInterrupt:
	GPIO.cleanup()
        
       