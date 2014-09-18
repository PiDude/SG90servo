
## SG90 servo

import RPi.GPIO as GPIO     ## Import GPIO library
import time
import os
import sys

GPIO.setmode(GPIO.BCM) ## Use board pin numbering

#pins are pulled up because the reed switches are ON by default.


GPIO.setup(25, GPIO.OUT)
p25=GPIO.PWM(25, 50)  # pin 18, and 50 Hz

p25.start(7.5) # set to neutral position - 7.5% duty cycle
#p.ChangeFrequency
#p.stop


time.sleep(2)

try:
    while True:
        for i in range(1, 26):
            p25.ChangeDutyCycle(i/2)
            time.sleep(0.04)
        for i in range(1, 26):
            p25.ChangeDutyCycle(14.5-(i/2))
            time.sleep(0.04)
    
except KeyboardInterrupt:
    p25.ChangeDutyCycle(7.5)
    p25.stop
    time.sleep(0.5)
    GPIO.cleanup()

