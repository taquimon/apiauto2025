import json
import logging
import requests

from config.config import url_base, headers
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestProject:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.project_list = []

    def test_create_project(self, test_log_name):
        """
        Test for create a project
        :param test_log_name:  log the test name
        """
        # body
        project_body = {
            "name": "Test Project from test",
        }
        # call endpoint using requests
        response = requests.post(
            url=f"{url_base}projects", headers=headers, json=project_body
        )
        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))
        self.project_list.append(response.json()["id"])
        # assertion
        assert response.status_code == 200

    def test_get_project(self, create_project, test_log_name):
        """
        Test for get a project
        :param create_project:   (str) Id of the project
        :param test_log_name:    (str) log the test name
        """
        # url for get the project
        url_get_project = f"{url_base}projects/{create_project}"
        LOGGER.debug(f"URL get project: {url_get_project}")

        # call GET endpoint (act)
        response = requests.get(url=url_get_project, headers=headers)
        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))
        # assertion
        assert response.status_code == 200

    def test_update_project(self, create_project, test_log_name):
        """
        Test for update a project
        :param create_project: (str) Id of the project
        :param test_log_name:  (str) log the test name
        """
        # url for update the project
        url_update_project = f"{url_base}projects/{create_project}"
        # boy for update project
        update_project_body = {
            "name": "Updated Project",
            "description": "Project description updated",
            "color": "yellow",
        }
        LOGGER.debug(f"URL update project: {url_update_project}")
        # call POST endpoint
        response = requests.post(
            url=url_update_project, headers=headers, json=update_project_body
        )
        LOGGER.debug("Response: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("Status Code: %s", str(response.status_code))
        # assertion
        assert response.status_code == 200

    def test_delete_project(self, create_project, test_log_name):
        """
        Test for delete a project
        :param create_project:  (str) Id of the project
        :param test_log_name:   (str) log the test name
        """
        url_delete_project = f"{url_base}projects/{create_project}"
        LOGGER.debug(f"URL delete project: {url_delete_project}")
        response = requests.delete(url=url_delete_project, headers=headers)
        # LOGGER.debug("Response: %s", response.json())
        LOGGER.debug("Status Code: %s", str(response.status_code))
        # assertion
        assert response.status_code == 204

    @classmethod
    def teardown_class(cls):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup projects
        LOGGER.info("Test Project teardown Class")
        for project_id in cls.project_list:
            url_delete_project = f"{url_base}projects/{project_id}"
            LOGGER.debug(f"URL delete project: {url_delete_project}")
            response = requests.delete(url=url_delete_project, headers=headers)
            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 204:
                LOGGER.debug("Project deleted")
