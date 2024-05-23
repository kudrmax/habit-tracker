import os

import requests
# from dotenv import load_dotenv

from tg_api import TG_API

whook = 'ec5c1df70ecdc7.lhr.life'

r = requests.get(f'https://api.telegram.org/bot{TG_API}/setWebhook?url=https://{whook}/')

print(r.json())
