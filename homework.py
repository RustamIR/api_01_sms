import time
import requests
from twilio.rest import Client
from dotenv import load_dotenv 
import os
load_dotenv()

def get_status(user_id):
    vk_token = os.getenv('vk_token')
    params = {
        'user_ids': user_id,
        'access_token': vk_token,
        'fields': 'online'
    }
    
    request = requests.post('https://api.vk.com/method/users.get', params=params).json()['response']
    status = request[0]['online']
    return status 

def sms_sender(sms_text):
    from twilio.rest import Client
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                     body='User online',
                                     from_=os.getenv("NUMBER_FROM"),
                                     to=os.getenv("NUMBER_TO")
    )
    return message.sid 

if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
