
from twilio.rest import Client
from dotenv import load_dotenv 
import os
load_dotenv()


account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_=os.getenv("NUMBER_FROM"),
                              to=os.getenv("NUMBER_TO")
                          )

print(message.sid)
