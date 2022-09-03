from twilio.rest import Client

account_sid = "<YOUR_SID>"
auth_token = "<YOUR_AUTH_TOKEN>"

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid,auth_token)

    def send_sms(self,message):
        message = self.client.messages.create(
            body=message,
            from_= "<FROM_NUMBER>",
            to= "<TO_NUMBER>",
        )
        print (message.sid)
