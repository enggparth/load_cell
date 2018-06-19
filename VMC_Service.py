import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Service_En=7
GPIO.setup(Service_En, GPIO.IN)

key_En=26
key_S1=05
key_S2=06
key_S3=13
key_S4=19
GPIO.setup(key_En, GPIO.OUT)#enable DeMux
GPIO.setup(key_S1, GPIO.OUT)#Select 1
GPIO.setup(key_S2, GPIO.OUT)#Select 2
GPIO.setup(key_S3, GPIO.OUT)#Select 3
GPIO.setup(key_S4, GPIO.OUT)#Select 4

GPIO.output(key_En, GPIO.HIGH)

service_sleep = 2
CE_sleep = 2
HM_sleep = 10

start_sleep = 1
end_sleep = 1.2

def key(arg):
    time.sleep(start_sleep)
    keys = ["1","2","3","4","5","6","7","8","9","*","0","#"]
    if keys[0] in arg:
        print("one")
        GPIO.output(key_S1, GPIO.LOW)
        GPIO.output(key_S2, GPIO.LOW)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.LOW)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[1] in arg:
        print("two")
        GPIO.output(key_S1, GPIO.LOW)
        GPIO.output(key_S2, GPIO.LOW)
        GPIO.output(key_S3, GPIO.LOW)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[2] in arg:
        print("three")
        GPIO.output(key_S1, GPIO.LOW)
        GPIO.output(key_S2, GPIO.LOW)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[3] in arg:
        print("four")
        GPIO.output(key_S1, GPIO.HIGH)
        GPIO.output(key_S2, GPIO.LOW)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.LOW)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[4] in arg:
        print("five")
        GPIO.output(key_S1, GPIO.HIGH)
        GPIO.output(key_S2, GPIO.LOW)
        GPIO.output(key_S3, GPIO.LOW)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[5] in arg:
        print("six")
        GPIO.output(key_S1, GPIO.HIGH)
        GPIO.output(key_S2, GPIO.LOW)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[6] in arg:
        print("seven")
        GPIO.output(key_S1, GPIO.LOW)
        GPIO.output(key_S2, GPIO.HIGH)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.LOW)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[7] in arg:
        print("eight")
        GPIO.output(key_S1, GPIO.LOW)
        GPIO.output(key_S2, GPIO.HIGH)
        GPIO.output(key_S3, GPIO.LOW)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[8] in arg:
        print("nine")
        GPIO.output(key_S1, GPIO.LOW)
        GPIO.output(key_S2, GPIO.HIGH)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[9] in arg:
        print("astrix")
        GPIO.output(key_S1, GPIO.HIGH)
        GPIO.output(key_S2, GPIO.HIGH)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.LOW)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[10] in arg:
        print("zero")
        GPIO.output(key_S1, GPIO.HIGH)
        GPIO.output(key_S2, GPIO.HIGH)
        GPIO.output(key_S3, GPIO.LOW)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    elif keys[11] in arg:
        print("hash")
        GPIO.output(key_S1, GPIO.HIGH)
        GPIO.output(key_S2, GPIO.HIGH)
        GPIO.output(key_S3, GPIO.HIGH)
        GPIO.output(key_S4, GPIO.HIGH)
        GPIO.output(key_En, GPIO.LOW)
    time.sleep(end_sleep)
    GPIO.output(key_En, GPIO.HIGH)
    return

def ClearErr():
    GPIO.setup(Service_En, GPIO.OUT)
    GPIO.output(Service_En, GPIO.LOW)
    time.sleep(service_sleep)
    sequence = ["9","*","0","*","#","#","#"]
    for i in range(0,len(sequence)):
        key(sequence[i])
	if i==3:
	   time.sleep(CE_sleep)
    GPIO.output(Service_En, GPIO.HIGH)
    GPIO.setup(Service_En, GPIO.IN)
    time.sleep(service_sleep)

def HomeMotor():
    #GPIO.output(Service_En, GPIO.LOW)
    GPIO.setup(Service_En, GPIO.OUT)
    GPIO.output(Service_En, GPIO.LOW)
    time.sleep(service_sleep)
    sequence = ["9","*","0","0","*","*","#","#","#","#"]
    for i in range(0,len(sequence)):
        key(sequence[i])
	if i==5:
	   time.sleep(HM_sleep)
    GPIO.setup(Service_En, GPIO.IN)

if sys.argv[1]=="CLEAR":
	ClearErr()
elif sys.argv[1]=="HOME":
	HomeMotor()
