from twilio.rest import Client
import os

class TwilioSMSClient(object):
    AUTH_SID = os.environ["PING_TWILIO_AUTH_SID"]
    AUTH_TOKEN = os.environ["PING_TWILIO_AUTH_TOKEN"]
    RECEIVERS = os.environ["PING_RECEIVERS"]
    SENDING_10DLC = os.environ["PING_TWILIO_10DLC"]

    def __init__(self):
        self.twilioClient = Client(self.AUTH_SID, self.AUTH_TOKEN)
    
    def notify(self, message):
        for receiver in self.RECEIVERS.split(','):
            self.twilioClient.api.account.messages.create(
                to=receiver,
                from_=self.SENDING_10DLC,
                body=message
            )

