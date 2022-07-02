import RPi.GPIO as GPIO
import time
import math


GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN)

light_sensor_pin = 13


light_value = 0
while(1):
    try:

     light_value = GPIO.input(light_sensor_pin)
     
        if light_value==0 or light_value==1:    
            if light_value==0:
                print("------------------")
                print ('Light Detected')
                print("------------------")
            else:
                print("------------------")
                print ('Light Not Detected')
                print("------------------")