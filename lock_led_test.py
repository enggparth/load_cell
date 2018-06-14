# External module imports
import RPi.GPIO as GPIO
import time
import sys
import os
# Pin Definitons:
DOOR_LOCK = [14,15,18,23]
LED_STRIP = [24,25,8,7]


# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_LOCK[0], GPIO.OUT)
GPIO.setup(DOOR_LOCK[1], GPIO.OUT)
GPIO.setup(DOOR_LOCK[2], GPIO.OUT)
GPIO.setup(DOOR_LOCK[3], GPIO.OUT)
GPIO.setup(LED_STRIP[0], GPIO.OUT)
GPIO.setup(LED_STRIP[1], GPIO.OUT)
GPIO.setup(LED_STRIP[2], GPIO.OUT)
GPIO.setup(LED_STRIP[3], GPIO.OUT)
#GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for door locks and led strips
GPIO.setwarnings(False)
GPIO.output(DOOR_LOCK[0], GPIO.LOW)
GPIO.output(DOOR_LOCK[1], GPIO.LOW)
GPIO.output(DOOR_LOCK[2], GPIO.LOW)
GPIO.output(DOOR_LOCK[3], GPIO.LOW)
GPIO.output(LED_STRIP[0], GPIO.LOW)
GPIO.output(LED_STRIP[1], GPIO.LOW)
GPIO.output(LED_STRIP[2], GPIO.LOW)
GPIO.output(LED_STRIP[3], GPIO.LOW)




def door_lock_0():
    GPIO.output(DOOR_LOCK[0],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(DOOR_LOCK[0],GPIO.LOW)
    time.sleep(1)
    print("Door 1 opened")
def door_lock_1():
    GPIO.output(DOOR_LOCK[1],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(DOOR_LOCK[1],GPIO.LOW)
    time.sleep(1)
    print("Door 2 opened")
def door_lock_2():
    GPIO.output(DOOR_LOCK[2],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(DOOR_LOCK[2],GPIO.LOW)
    time.sleep(1)
    print("Door 3 opened")
def door_lock_3():
    GPIO.output(DOOR_LOCK[3],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(DOOR_LOCK[3],GPIO.LOW)
    time.sleep(1)
    print("Door 4 opened")
#Main prg to open door
try:
    
    if sys.argv[1]== "1":
        door_lock_0()
        
    elif sys.argv[1]== "2":
        door_lock_1()
        
    elif sys.argv[1]== "3":
        door_lock_2()
        
    elif sys.argv[1]== "4":
        door_lock_3()
        
    
except KeyboardInterrupt:
    print("Over")

finally:
    GPIO.cleanup()