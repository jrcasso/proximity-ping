#!/usr/bin/python
from rpi.sensor import SensorGPIO
from notifers.client import TwilioSMSClient
import os
import time

class WindowAlarm(SensorGPIO):
    def __init__(self):
        super().__init__()
        self.TIMEOUT = int(os.getenv("PING_TIMEOUT", 10))
        self.notifier = TwilioSMSClient()

    def loop(self):
        seconds = 0
        while True:
            objectIsFar = self.get_sensor_state()
            if objectIsFar:
                time.sleep(1.000)
                seconds += 1         
            else:
                time.sleep(0.050)
                seconds = 0

            if (seconds >= self.TIMEOUT):
                seconds = 0
                print("Exceeded timeout! Notifying...")
                self.notifier.notify("You left the window open IDIOT")
            
            print(seconds)
