# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="God bless Africa!.",
                     from_='TWILIO_PHONE_NUMBER',
                     to='VERIFIED_PHONE_NUMBER'

                 )

print(message.sid)
