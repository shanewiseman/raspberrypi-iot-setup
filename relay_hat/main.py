import RPi.GPIO as GPIO
import time


RELAY_1 = 26 
RELAY_2 = 20 
RELAY_3 = 21 

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_1, GPIO.OUT)
GPIO.setup(RELAY_2, GPIO.OUT)
GPIO.setup(RELAY_3, GPIO.OUT)

for _ in range(10):

    GPIO.output(RELAY_1, GPIO.HIGH)
    GPIO.output(RELAY_2, GPIO.HIGH)
    GPIO.output(RELAY_3, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAY_1, GPIO.LOW)
    GPIO.output(RELAY_2, GPIO.LOW)
    GPIO.output(RELAY_3, GPIO.LOW)
    time.sleep(1)

