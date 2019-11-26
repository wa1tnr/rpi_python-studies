#!/bin/sh

# github.com/raspberrypi/linux/issues/2517 xset

xset_setup () {
    xset -display :0 dpms force on
    xset -display :0 s blank
    xset -display :0 s on
    xset -display :0 s 500 500
    xset -display :0 dpms 500 500 500
    xsetroot -display :0 -solid black
    xset -display :0 s on
    xset -display :0 s 500 500
    xset -display :0 q
    # edit the next line to use the full path to the script
    tv-recycle.sh
    date > .semaphore-xset_subr
    sleep  530 ; xset -display :0 dpms force off # turn it off entirely? TRIAL
}

# wake the screen:
date > .semaphore-xset

# wake the display
xset -display :0 s reset

# setup timing and blanking after a reset:
xset_setup
