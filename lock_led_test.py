# External module imports
import RPi.GPIO as GPIO
import time
import sys
import os
# Pin Definitons:
DOOR_LOCK = [14,15,18,23]
LED_STRIP = [24,25,8,7]
sleep_lock = 0.25
sleep_led = 0.5
sleep = 1
FB_LOCK = [2,3,4,17]



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
GPIO.setup(FB_LOCK[0],GPIO.IN,pull_up_down=GPIO.PUD_UP)

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



# pwm setup
#pwm_led_1 = GPIO.PWM(24,50)
#pwm_led_2 = GPIO.PWM(25,50)
#pwm_led_3 = GPIO.PWM(8,50)
#pwm_led_4 = GPIO.PWM(7,50)





def door_lock_0():
    GPIO.output(DOOR_LOCK[0],GPIO.HIGH)
    time.sleep(sleep_lock)
    GPIO.output(DOOR_LOCK[0],GPIO.LOW)
    time.sleep(1)
    print("Door 1 opened")
def door_lock_1():
    GPIO.output(DOOR_LOCK[1],GPIO.HIGH)
    time.sleep(sleep_lock)
    GPIO.output(DOOR_LOCK[1],GPIO.LOW)
    time.sleep(1)
    print("Door 2 opened")
def door_lock_2():
    GPIO.output(DOOR_LOCK[2],GPIO.HIGH)
    time.sleep(sleep_lock)
    GPIO.output(DOOR_LOCK[2],GPIO.LOW)
    time.sleep(1)
    print("Door 3 opened")
def door_lock_3():
    GPIO.output(DOOR_LOCK[3],GPIO.HIGH)
    time.sleep(sleep_lock)
    GPIO.output(DOOR_LOCK[3],GPIO.LOW)
    time.sleep(1)
    print("Door 4 opened")

def led_strip_1():
    GPIO.output(LED_STRIP[0], GPIO.HIGH)
    time.sleep(sleep_led)
    GPIO.output(LED_STRIP[0], GPIO.LOW)
    time.sleep(sleep_led)
    
def led_strip_2():
    GPIO.output(LED_STRIP[1], GPIO.HIGH)
    time.sleep(sleep_led)
    GPIO.output(LED_STRIP[1], GPIO.LOW)
    time.sleep(sleep_led)
    
def led_strip_3():
    GPIO.output(LED_STRIP[2], GPIO.HIGH)
    time.sleep(sleep_led)
    GPIO.output(LED_STRIP[2], GPIO.LOW)
    time.sleep(sleep_led)
def led_strip_4():
    GPIO.output(LED_STRIP[3], GPIO.HIGH)
    time.sleep(sleep_led)
    GPIO.output(LED_STRIP[3], GPIO.LOW)
    time.sleep(sleep_led)
#Main prg to open door
try:
    
    if sys.argv[1]== "1":
        door_lock_0()                                        #open the lock
        start = time.time()                                  #start the timers
        for i in range (0,5):                                #led blink for particular block
                    led_strip_1()                            #led blink func              
        fb_status_1 = GPIO.input(FB_LOCK[0])
        while fb_status_1:
            print("Door is opened")
            end = time.time()
            if (end-start) > 20:
                print ("Door is still opened")
                for i in range (0,5):                                #led blink for particular block
                    led_strip_1()
        
                        
        else:
            print("Closed the door")
            
            
    elif sys.argv[1]== "2":
        door_lock_1()
        for i in range (0,5):
                    led_strip_2()
    elif sys.argv[1]== "3":
        door_lock_2()
        for i in range (0,5):
                    led_strip_3()
    elif sys.argv[1]== "4":
        door_lock_3()
        for i in range (0,5):
                    led_strip_4()
    elif sys.argv[1] == "fb":
        while True:
            fb_status_1 = GPIO.input(FB_LOCK[0])
            if fb_status_1 == False:
                start = time.time()
                print("Door opened")
                end = time.time
                
            else:
                print("Door closed")
    
        
#    pwm_led_1.start(50)
#   pwm_led_1.ChangeDutyCycle(20)
#    time.sleep(2)
#    pwm_led_1.ChangeDutyCycle(40)
#    time.sleep(2)
#    pwm_led_1.ChangeDutyCycle(60)
#    time.sleep(2)
#    pwm_led_1.ChangeDutyCycle(80)
#    time.sleep(2)
#    pwm_led_1.ChangeDutyCycle(100)
#    time.sleep(2)
#    pwm_led_1.stop()
    
except KeyboardInterrupt:
    print("Over")

finally:
    GPIO.cleanup()