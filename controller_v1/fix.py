
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.OUT)
time.sleep(1)
gpio.setup(23, gpio.OUT)

gpio.output(23, gpio.HIGH)
gpio.output(24, gpio.HIGH)
#exit(1)

gpio.output(24, gpio.HIGH)
time.sleep(1)
gpio.output(23, gpio.LOW)
while True:
    
    time.sleep(10)
    gpio.output(23, gpio.HIGH)
    time.sleep(1)
    gpio.output(24, gpio.LOW)
    time.sleep(10)
    gpio.output(24, gpio.HIGH)
    time.sleep(1)
    gpio.output(23, gpio.LOW)
