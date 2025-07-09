import json
import logging

from helper.validate_response import ValidateResponse
from utils.logger import get_logger
from wiremock.server import WireMockServer
from helper.rest_client import RestClient

LOGGER = get_logger(__name__, logging.DEBUG)


class WireMockStub:
    def __init__(self):
        self.wiremock = WireMockServer()
        self.rest_client = RestClient()
        self.validate = ValidateResponse()
        self.wiremock.start()

    def create_stub(self, json_file=None):
        url_mappings = f"http://localhost:{self.wiremock.port}/__admin/mappings"
        LOGGER.debug(f"url_mappings: {url_mappings}")
        json_data = self.validate.read_input_data(
            "/home/predator/ETJala/APIAutomation/src/api/input_json/get_label_stub.json"
        )
        response = self.rest_client.send_request(
            "POST", url_mappings, data=json.dumps(json_data)
        )
        LOGGER.debug(f"response: {response}")
        return self.wiremock, response

    def get_stub(self):
        url_mappings = "http://localhost:8080/__admin/mappings"
        response = self.rest_client.send_request("GET", url_mappings)
        LOGGER.debug("Response: %s", json.dumps(response, indent=4))
        LOGGER.debug(
            "Status Code: %s", response["body"]["mappings"][0]["response"]["status"]
        )
        assert response["body"]["mappings"][0]["response"]["status"] == 200


if __name__ == "__main__":
    mock_stub = WireMockStub()
    mock_stub.create_stub()
