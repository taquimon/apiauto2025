import json
import logging

from tenacity import retry, stop_after_attempt, wait_exponential

from helper.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestFastAPI:
    @classmethod
    def setup_class(cls):
        cls.url_fast_api = "http://127.0.0.1:8000/"
        headers_fast_api = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }

        fast_api_body = {
            "grant_type": "password",
            "password": "password123!",
            "username": "etaquichiri",
            "scope": "",
            "client_id": "",
            "client_secret": "",
        }
        cls.rest_client = RestClient()
        response = cls.rest_client.send_request(
            "POST",
            url=f"{cls.url_fast_api}token",
            headers=headers_fast_api,
            data=fast_api_body,
        )
        LOGGER.debug("Response %s", json.dumps(response["body"], indent=4))
        cls.token = response["body"]["access_token"]

        cls.headers = {
            "accept": "application / json",
            "Authorization": f"Bearer {cls.token}",
        }

    @retry(
        stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def test_get_users(self):
        url_fast_api_users = f"{self.url_fast_api}users"
        response = self.rest_client.send_request(
            "GET", url=url_fast_api_users, headers=self.headers
        )
        LOGGER.debug(response)
        LOGGER.debug("Response %s", json.dumps(response["body"], indent=4))
