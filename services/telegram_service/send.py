import requests

from tg_api import TG_API, WHOOK

message_uel = f'https://api.telegram.org/bot{TG_API}/sendMessage'

data = {
    'chat_id': 1948080279,
    'text': 'Response'
}

req = requests.post(message_uel, data=data)
