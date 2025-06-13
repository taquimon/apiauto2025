import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("TOKEN_TODO")
url_base = os.getenv("URL_BASE")

headers = {
    "Authorization": "Bearer {}".format(api_token),
}
