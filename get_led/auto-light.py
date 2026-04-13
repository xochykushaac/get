import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

led = 26
trans = 6


GPIO.setup(trans, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, not GPIO.input(trans))
    time.sleep(0.05) 