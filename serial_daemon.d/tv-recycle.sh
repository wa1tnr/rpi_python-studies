#!/bin/sh

# /opt/vc/bin/tvservice -o # power off HDMI

# display is OFF now.
# sleep 16

# display may be truly OFF now.
/opt/vc/bin/tvservice -p # invoke preferred mode HDMI
fbset -depth 8
sleep 1
fbset -depth 32
# xrefresh -d :0.0
# fbset -xres 720
# fbset -yres 400

# Display has been powered on.  Automatically power it off after a timer expires:
# edit the next line to use the full path to the script
exec _run_timed_hdmi_off.sh > /dev/null 2>&1 &
