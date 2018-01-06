# woo_woo.py
# makes a woo woo noise pattern
# Sat  6 Jan 21:15:11 UTC 2018

# Pin 5 - piezo buzzer   Pin 6 - LED

from Adafruit_Seesaw import Seesaw
import time

ss = Seesaw()

def wooW():
    for pulse in range(1, 250, 1):
        ss.analog_write(5, pulse)
        time.sleep(.004)
        ss.analog_write(6, pulse)
        time.sleep(.004)

def Woow():
    for pulse in range(250, 1, -1):
        ss.analog_write(5, pulse)
        time.sleep(.004)
        ss.analog_write(6, pulse)
        time.sleep(.004)


iterations = 1 + 24 # specifying it this way gives
                    # an expectation of twenty-four-ish-ness

def pargram():
    for index in range(15, iterations, 3): # demo non-traditional range specifications
        print(index)
        wooW()
        Woow()
        time.sleep(1.2)

def cleanup():
    ss.analog_write(5, 0) # off and quiet
    time.sleep(.004)
    ss.analog_write(6, 0) # off and dark
    time.sleep(.004) # be nice to others

pargram()
cleanup()
# end
