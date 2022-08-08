#!/usr/bin/python
from alarms.window import WindowAlarm
import sys

if __name__ == "__main__":
    try:
        alarm = WindowAlarm()
        alarm.loop()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        alarm.cleanup()
