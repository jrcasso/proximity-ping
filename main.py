#!/usr/bin/python
from alarms.window import WindowAlarm
import sys

if __name__ == "__main__":
    try:
        # TODO: [REFACTOR] Generalize the approach. Object interdepedencies
        # are not abstracted and should be decoupled so that a generic
        # configuration can be used. Such a configuration might be a YAML
        # specification corresponding to different alarm types and client
        # notifiers for this pico to run many simultaneously. All classes
        # currently make implicit assumptions that can instead be made to
        # be generic and plug-and-play from a parsed configuration.
        alarm = WindowAlarm()
        alarm.loop()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        alarm.cleanup()
