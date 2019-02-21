Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Libraries
import RPi.GPIO as GPIO  # Importing RPi library to use the GPIO pins
import time              # Importing sleep from time library
GPIO.setwarnings(False)
#GPIO mode
GPIO.setmode(GPIO.BCM)   # We are using the BCM pin numbering
GPIO.setup(2,GPIO.OUT)   # Declaring pin 2 as output pin
GPIO.setup(26,GPIO.OUT)  # Declaring pin 2 as output pin
pwm = GPIO.PWM(2, 100)   # Created a PWM object 
pwm = GPIO.PWM(26, 100)  # Created a PWM object
try:
        while True:      # Loop will run forever
            GPIO.output(2,GPIO.HIGH)
            GPIO.output(26,GPIO.HIGH)
            time.sleep(1)              # Delay of 1Second
            GPIO.output(2,GPIO.LOW)
            GPIO.output(26,GPIO.LOW)
            time.sleep(0.1)            # Delay of 1 Second

# If keyboard Interrupt (CTRL-C) is pressed
except KeyboardInterrupt:
        pwm.stop()        #Stop PWM  
        GPIO.cleanup()    #All the pins will be turned off


