from twilio.rest import Client
#from credentials import account_sid, auth_token, my_cell, my_twilio

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
my_cell = 'VERIFIED_PHONE_NUMBER'
my_twilio = 'TWILIO_PHONE_NUMBER'
client = Client(account_sid, auth_token)

my_msg = "God bless Africa!."

message = client.messages.create(to=my_cell, from_=my_twilio,
                                 body=my_msg)