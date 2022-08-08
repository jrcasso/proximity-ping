import RPi.GPIO as GPIO
import os

class SensorGPIO:
    PIN_SENSOR = os.getenv("PING_PIN_SENSOR", 17)

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SensorGPIO.PIN_SENSOR, GPIO.IN)

    def get_sensor_state(self):
        return GPIO.input(self.PIN_SENSOR)

    def cleanup(self):
        GPIO.cleanup()
