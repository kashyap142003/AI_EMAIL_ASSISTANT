"""import requests
from requests.exceptions import Timeout

BASE_URL = "https://catfact.ninja/fact"

MAX_RETRIES = 3

for i in range(MAX_RETRIES):    
    try:
        r = requests.get(BASE_URL, timeout = 0.3)

        print(r.text)
        print(r.status_code)
        break
    except Timeout as to:
        print("Timeout Error")

else:
    print("All retries failed")"""


import requests
import config

url = config.user()

r = requests.get(url)
print(r.json())
print(type(r.json()))