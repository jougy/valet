import RPi.GPIO as GPIO
from time import sleep
import sys
import os
led01 = 18
MotorA_PIN = 12
MotorB_PIN = 13
en = 25
bt1 = 15
temp1=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led01,GPIO.OUT)
GPIO.setup(MotorA_PIN,GPIO.OUT)
GPIO.setup(MotorB_PIN,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.setup(bt1, GPIO.IN)
GPIO.output(MotorA_PIN,GPIO.LOW)
GPIO.output(MotorB_PIN,GPIO.LOW)
GPIO.output(led01,GPIO.LOW)
p=GPIO.PWM(en,100)

p.start(25)

def frente():
	GPIO.output(led01,GPIO.HIGH)
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	print("frente")
def tras():
	GPIO.output(led01,GPIO.LOW)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.HIGH)
	print("tras")

def parar():
	print("stop")
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)



