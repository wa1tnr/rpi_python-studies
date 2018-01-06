# buzz_slow.py
# raspy crickety thing
# piezo buzzer on PWM Pin 5 - Seesaw
# Sat  6 Jan 21:13:55 UTC 2018

# Pin 5 - piezo buzzer   Pin 6 - LED (unused here)

from Adafruit_Seesaw import Seesaw
import time

ss = Seesaw()

def subr():
    while True:
        for pulse in range(1, 9, 1):
            ss.analog_write(5, pulse)
            time.sleep(.002)
subr()
# end
