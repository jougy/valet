import RPi.GPIO as gpio
import time
gpio.setmode (gpio.BOARD)
gpio.setup (37, gpio.OUT)
gpio.setup (38, gpio.OUT)

m1 = gpio.PWM (37, 1000)
m2 = gpio.PWM (38, 1000)
m1.start(0)
m2.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            m1.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range (100, -1, -5):
            m1.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(0, 101, 5):
            m2.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range (100, -1, -5):
            m2.ChangeDutyCycle(dc)
            time.sleep(0.1)
            
except KeyboardInterrupt:
    pass
m1.stop()

    