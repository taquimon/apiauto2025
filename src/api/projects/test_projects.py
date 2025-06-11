import logging
import requests
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestProject:

    def test_create_project(self):
        pass

    def test_get_project(self, get_data_api, create_project):
        # call endpoint
        url_get_project = f"{get_data_api['url_base']}projects/{create_project}"
        LOGGER.debug(f"url_get_project: {url_get_project}")
        response = requests.get(url=url_get_project,
                                 headers=get_data_api['headers'])
        LOGGER.debug("Response: %s", response.json())
        LOGGER.debug("Status Code: %s", str(response.status_code))
        assert response.status_code == 200

    def test_update_project(self):
        pass

    def test_delete_project(self):
        pass
