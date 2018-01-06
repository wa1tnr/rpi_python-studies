# int_woo_woo.py
# makes a woo woo noise pattern

# INTEGER considerations explored.

# Sat  6 Jan 21:25:42 UTC 2018

# Pin 5 - piezo buzzer   Pin 6 - LED

# The LED gets a series resistor of 1k and the buzzer
# was given one of about 470 ohms.

# An effort was made to make the demo visually somewhat
# more interesting.  This is perhaps best appreciated if
# the LED optics are used to rear-project light onto a
# sheet of ordinary white paper.

# The changes in brightness may be made more apparent, then.

from Adafruit_Seesaw import Seesaw
import time

ss = Seesaw()

def wooW():
    for pulse in range(1, 1014, 4):
        scaled_pulse = int(pulse / 4)
        if not (isinstance(scaled_pulse, str)):
            if not (type(scaled_pulse) == int):
                print("critters.  them critters.")
            else:
                print("INT.")
                valued_pulse = scaled_pulse -7
                print(scaled_pulse, valued_pulse)
                none = 0 # no operation at all -- placeholder only

        ss.analog_write(5, scaled_pulse)

        # a bit more variety, when uncommented:
        # comment out below
        if (pulse < 100):
            time.sleep(.14)
        if (pulse < 200):
            time.sleep(.07)
        if (pulse < 300):
            time.sleep(.05)
        if (pulse < 400):
            time.sleep(.02)
        if (pulse < 500):
            time.sleep(.009)
        # comment out above

        time.sleep(.04)
        time.sleep(.004)
        ss.analog_write(6, pulse / 4)
        time.sleep(.004)

def Woow():
    for pulse in range(1014, 1, -4):
        ss.analog_write(5, pulse / 4)
        time.sleep(.004)
        ss.analog_write(6, pulse / 4)
        time.sleep(.004)


iterations = 1 + 24

def pargram():
    for index in range(15, iterations, 3):
        print(index)
        wooW()
        Woow()
        time.sleep(1.2)

def cleanup():
    ss.analog_write(5, 0) # off and quiet and dark
    time.sleep(.004)
    ss.analog_write(6, 0) # off and quiet and dark
    time.sleep(.004) # be nice to others

pargram()
cleanup()
# end
