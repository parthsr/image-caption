import time
import RPi.GPIO as GPIO
import os


# tell the GPIO module that we want to use the 
# chip's pin numbering scheme
GPIO.setmode(GPIO.BCM)

# setup pin 25 as an output
GPIO.setup(23,GPIO.IN)

old  = False
while True:
	if GPIO.input(23) and not old:
     		print "button true"
		os.system('python TakePicture.py')
		time.sleep(0.1)
		os.system('python microsoft.py')
	old = GPIO.input(23)

	time.sleep(0.1)

GPIO.cleanup()

