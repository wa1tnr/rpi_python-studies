# offnow.py
# just about complete silence from the piezo
# run when finished - PWM generally keeps going without a running program
# Sat  6 Jan 21:14:22 UTC 2018

# Pin 5 - piezo buzzer   Pin 6 - LED

from Adafruit_Seesaw import Seesaw
import time

ss = Seesaw()

ss.analog_write(5, 0) # piezo buzzer quiet
time.sleep(.1)
ss.analog_write(6, 0) # LED off
