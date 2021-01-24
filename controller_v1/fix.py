
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

gpio.setup(27, gpio.IN, gpio.PUD_UP)
#gpio.setup(18, gpio.OUT)

while True:
    print(gpio.input(27))
    #gpio.output(18, gpio.LOW)
    time.sleep(1)
