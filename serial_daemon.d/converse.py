#!/usr/bin/python3.5

# github.com/raspberrypi/linux/issues/2517 xset

import serial
import sys
import os
import time

# put display to sleep 180 seconds from now:
# edit the next line to use the full path to the script
os.system("_run_timed_hdmi_off.sh")
sys.stdout.write('H')
sys.stdout.write(' ')
sys.stdout.flush()

def xset_setup():
    # this script spawns another in the background
    # edit the next line to use the full path to the script
    os.system("tv-recycle.sh")
    # next two lines are commented out
    # edit the next line to use the full path to the script
    # os.system("_run_xset.sh")

# xset_setup()

with serial.Serial(port='/dev/ttyS0', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0) as ser:
    rutroh = 0
    while -1:
        x = ser.read()

        xp = str(x)

        while (xp[-2:-1] == "+"):
            print('+', end='', flush=True)
            rutroh = rutroh + 1 # require three consecutive +'s to trigger an ESCape
            if (rutroh == 3):
                rutroh = 0
                print(" SYSTEM ESCAPE: +++ detected.", flush=True)
                xset_setup()
                print("xset_setup() was called.")
                x = ser.read()
                xp = str(x)
                break
            x = ser.read()
            xp = str(x)

        rutroh = 0 # enforce three consecutive +'s requirement
        # if it's any char except CR or LF, print it
        if ((xp[-3:-1] != "\\n") & (xp[-3:-1] != "\\r")):
            print (xp[-2:-1], end='', flush=True)

        # if it was a newline, print its equivalent
        if (xp[-3:-1] == "\\n"):
            print("", flush=True)
