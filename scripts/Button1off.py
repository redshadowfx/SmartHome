#!/usr/bin/env python2.7



import RPi.GPIO as GPIO
import time
import cgitb
cgitb.enable() 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

state = True

GPIO.output(21,True)
	
