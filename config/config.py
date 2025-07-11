import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("TOKEN_TODO")
url_base = os.getenv("URL_BASE")
web_hook = os.getenv("WEB_HOOK")
influxdb_token = os.getenv("INFLUXDB_TOKEN")
headers = {
    "Authorization": "Bearer {}".format(api_token),
}
