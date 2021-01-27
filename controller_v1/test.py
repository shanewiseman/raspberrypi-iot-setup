import RPi.GPIO as gpio
import sys
import time
import datetime


RELAY_1 = 26 
RELAY_2 = 20 
RELAY_3 = 21 

INPUT_1 = 17
INPUT_2 = 27
INPUT_3 = 22

OUTPUT_1 = 23
OUTPUT_2 = 24

gpio.setmode(gpio.BCM)
gpio.setup(RELAY_1, gpio.OUT)
gpio.setup(RELAY_2, gpio.OUT)
gpio.setup(RELAY_3, gpio.OUT)
gpio.output(RELAY_1, gpio.HIGH)
gpio.output(RELAY_2, gpio.HIGH)
gpio.output(RELAY_3, gpio.HIGH)


gpio.setup(OUTPUT_1, gpio.OUT)
gpio.setup(OUTPUT_2, gpio.OUT)
gpio.output(OUTPUT_1, gpio.HIGH)
gpio.output(OUTPUT_2, gpio.HIGH)

gpio.setup(INPUT_1, gpio.IN, gpio.PUD_UP)
gpio.setup(INPUT_2, gpio.IN, gpio.PUD_UP)
gpio.setup(INPUT_3, gpio.IN, gpio.PUD_UP)


FURNACE_SWITCH = RELAY_1
ZONE_3_SWITCH = RELAY_2
HOT_WATER_SWITCH = RELAY_3
FAN_LOW = OUTPUT_1
FAN_HIGH = OUTPUT_2

ZONE_1_CALL = INPUT_2
ZONE_2_CALL = INPUT_1
HOT_WATER_CALL = INPUT_3
#exit(0)
print("Started")
def input_call(zone):
    return not gpio.input(zone)

def toggle_switch(switch, enable):
    mode = gpio.LOW if enable else gpio.HIGH
    gpio.output(switch, mode) 


z1 = False
z2 = False
while True:
    try:

        if input_call(ZONE_1_CALL) and not z1:
            print("Zone 1 Start: {}".format(input_call(ZONE_1_CALL)))
            toggle_switch(ZONE_3_SWITCH, True)
            z1 = True
            ct = datetime.datetime.now() 
            print("current time:-", ct)
        elif not input_call(ZONE_1_CALL) and z1:
            print("Zone 1 End: {}".format(input_call(ZONE_1_CALL)))
            toggle_switch(ZONE_3_SWITCH, False)
            z1 = False
            ct = datetime.datetime.now() 
            print("current time:-", ct)


        if input_call(ZONE_2_CALL) and not z2:
            print("Zone 2 Start: {}".format(input_call(ZONE_2_CALL)))
            z2 = True 
            ct = datetime.datetime.now() 
            print("current time:-", ct)
        elif not input_call(ZONE_2_CALL) and z2:
            print("Zone 2 End: {}".format(input_call(ZONE_2_CALL)))
            z2 = False
            ct = datetime.datetime.now() 
            print("current time:-", ct)

        if input_call(ZONE_1_CALL) or input_call(ZONE_2_CALL):
            heat_call = True
        else:
            heat_call = False

        sys.stdout.flush()
###############################################################################
        
        if not input_call(FURNACE_SWITCH) and heat_call:
            print("HEAT ON")
            ct = datetime.datetime.now() 
            print("current time:-", ct)
            toggle_switch(FURNACE_SWITCH, True)

            c_time = datetime.datetime.now().time()
            if datetime.time(9,0) >= c_time or datetime.time(18,0) <= c_time:
                print("FAN HIGH")
                toggle_switch(FAN_LOW, False)
                time.sleep(1)
                toggle_switch(FAN_HIGH, True)
            else:
                print("FAN LOW")
                toggle_switch(FAN_LOW, True)

            print("\n\n")


        elif input_call(FURNACE_SWITCH) and not heat_call:
            print("HEAT OFF")
            ct = datetime.datetime.now() 
            print("current time:-", ct)
            print("\n\n")
            toggle_switch(FURNACE_SWITCH, False)
            toggle_switch(FAN_HIGH, False)
            time.sleep(1)
            toggle_switch(FAN_LOW, True)



        sys.stdout.flush()
################################################################################

        water_call = input_call(HOT_WATER_CALL)

        if not input_call(HOT_WATER_SWITCH) and water_call:
            toggle_switch(HOT_WATER_SWITCH, True)
            print("WATER ON")
            ct = datetime.datetime.now() 
            print("current time:-", ct)
            print("\n\n")
        elif input_call(HOT_WATER_SWITCH) and not water_call:
            toggle_switch(HOT_WATER_SWITCH, False)
            print("WATER OFF")
            ct = datetime.datetime.now() 
            print("current time:-", ct)

            print("\n\n")
        sys.stdout.flush()
        time.sleep(1)
    except KeyboardInterrupt:
        gpio.cleanup()
        exit(0)
