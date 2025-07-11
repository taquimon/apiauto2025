import logging

from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger
from utils.wiremock_stub import WireMockStub

LOGGER = get_logger(__name__, logging.DEBUG)


class TestLabel:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.project_list = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.wiremock = WireMockStub()

        cls.url_base_mock = "http://localhost:"

    def test_get_label(self, test_log_name):
        wiremock, stub = self.wiremock.create_stub("get_label")

        stub_id = stub["body"]["id"]
        url_get_labels = (
            f"{self.url_base_mock}{wiremock.port}/__admin/mappings/{stub_id}"
        )
        LOGGER.debug(f"URL get label: {url_get_labels}")
        response = self.rest_client.send_request("GET", url_get_labels)
        LOGGER.debug(f"response: {response}")

        # assertion
        assert response["status_code"] == 200
