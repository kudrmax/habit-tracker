import os

import requests
# from dotenv import load_dotenv

from tg_api import TG_API
from tg_api import WHOOK

r = requests.get(f'https://api.telegram.org/bot{TG_API}/setWebhook?url=https://{WHOOK}/')

print(r.json())
