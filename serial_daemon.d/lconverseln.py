#!/usr/bin/python3.5
import serial

with serial.Serial(port='/dev/ttyS0', baudrate=38400, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0) as ser:
    while -1:
        x = ser.readline()
        if (x == b'+++  ok\r\n'):
            xp = str(x)
            print(xp[2:-5])
            print ("saw the plus thrice escape")
        else:
            xp = str(x)
            print(xp[2:-5])
