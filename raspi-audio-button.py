#!/usr/bin/env python
from time import sleep
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
   if ( GPIO.input(24) != 0 ):
     print "24 pressed"
     os.system('mpg321 Booing.mp3 &')
     sleep(2.51);
   if ( GPIO.input(25) != 0 ):
     print "25 pressed"
     os.system('mpg321 Cheering.mp3 &')
     sleep(2.51);
