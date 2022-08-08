#!/usr/bin/python
import RPi.GPIO as GPIO
import time

PIN_SENSOR = 17
PIN_PIEZO = 18
TIMEOUT = 3

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_PIEZO, GPIO.OUT)
    GPIO.setup(PIN_SENSOR, GPIO.IN)

def loop():
    while True:
        objectIsClose = GPIO.input(PIN_SENSOR)
        if not objectIsClose:
            time.time.sleep(1000)
            seconds += 1         
        else:
            time.time.sleep(50)
            seconds = 0

        if (seconds >= TIMEOUT):
            print("Exceeded timeout!")
            GPIO.output(PIN_PIEZO, True)
        else:
            GPIO.output(PIN_PIEZO, False)
        
        print(seconds)

if __name__ == "__main__":
    try:
        setup()
        loop()
    finally:
        GPIO.cleanup()
