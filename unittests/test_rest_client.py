import json
import logging
import unittest

from helper.rest_client import RestClient
from utils.logger import get_logger
from config.config import url_base, headers

LOGGER = get_logger(__name__, logging.DEBUG)


class TestRestClient(unittest.TestCase):
    def test_get_rest_client(self):
        LOGGER.info("TestRestClient")
        rest_client = RestClient()
        response = rest_client.send_request(
            "GET", url=url_base + "projects", headers=headers
        )
        LOGGER.debug(json.dumps(response, indent=4))

    def test_get_rest_client_negative(self):
        LOGGER.info("TestRestClient")
        rest_client = RestClient()
        response = rest_client.send_request(
            "GET", url=url_base + "projects/tewrwerwerw", headers=headers
        )
        LOGGER.debug(json.dumps(response, indent=4))

    def test_get_rest_client_create_project_without_body_negative(self):
        LOGGER.info("TestRestClient")
        rest_client = RestClient()
        response = rest_client.send_request(
            "POST", url=url_base + "projects", headers=headers
        )
        LOGGER.debug(json.dumps(response, indent=4))
