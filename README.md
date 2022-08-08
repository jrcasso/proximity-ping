How to use:

1. Get a proximity sensor.
2. Put it somewhere interesting (e.g. a window you left open)
3. Clone this project onto your Raspberry Pi
4. Define environment variables:

|Environment Variable|Default|Description|
|-|-|-|
|PING_TWILIO_AUTH_SID| None (required) | Twilio authorization SID for notifications.|
|PING_TWILIO_AUTH_TOKEN| None (required) | Twilio authorization token for notifications. |
|PING_RECEIVERS| None (required) |Comma-separated list of 10 digit phone numbers to receive notifications (e.g. "+12223334444,+23334445555")|
|PING_TWILIO_10DLC| None (required) | Registered Twilio 10 digit phone number (e.g. "+12223334444)" |
|PING_TIMEOUT (seconds) | 10 | After the sensor has been tripped for this duration, a notification will be sent.|

5. Change directory to the project and run `./main.py`. You will get SMS notifications when the proximity sensor is tripped for longer than `PING_TIMEOUT`.
