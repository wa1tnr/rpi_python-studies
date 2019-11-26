#!/bin/sh

sleep 1800 # half an hour before a power off event
/opt/vc/bin/tvservice -o # power off HDMI
exit 0


# - - - -   nothing below this line will run   - - - - 
# display is OFF now.
# sleep 16

# display may be truly OFF now.

# WAKE the display as required:
/opt/vc/bin/tvservice -p # invoke preferred mode HDMI
fbset -depth 8 # fbset needs to temporarily be changed from the default, someone stated ;)
sleep 1
fbset -depth 32

# not required:
# xrefresh -d :0.0
# fbset -xres 720
# fbset -yres 400

