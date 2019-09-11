import RPi.GPIO as GPIO
from time import sleep
import sys
import os

MotorA_PIN = 12
MotorB_PIN = 13
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(MotorA_PIN,GPIO.OUT)
GPIO.setup(MotorB_PIN,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(MotorA_PIN,GPIO.LOW)
GPIO.output(MotorB_PIN,GPIO.LOW)



