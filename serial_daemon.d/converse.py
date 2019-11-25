#!/usr/bin/python3.5
import serial
import sys
import os
import time

sys.stdout.write('H')
sys.stdout.flush()

with serial.Serial(port='/dev/ttyS0', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0) as ser:
    rutroh=0
    while -1:
        x = ser.read()

        xp = str(x)

        while (xp[-2:-1] == "+"):
            print('+', end='', flush=True)
            rutroh = rutroh + 1
            if (rutroh == 3):
                rutroh = 0
                print("SYSTEM ESCAPE: +++ detected.", flush=True)
                # wake the screen:
                os.system("xset s reset")
                # time.sleep(seconds)
                time.sleep(1)
                os.system("xset s on s 900")
                print("xset s reset -- was executed and a new 900 second timeout is instantiated.")
                x = ser.read()
                xp = str(x)
                break
            x = ser.read()
            xp = str(x)

        rutroh = 0
        if ((xp[-3:-1] != "\\n") & (xp[-3:-1] != "\\r")):
            print (xp[-2:-1], end='', flush=True)

        if (xp[-3:-1] == "\\n"):
            print("", flush=True)
