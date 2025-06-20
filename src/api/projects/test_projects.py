import json
import logging

import allure
import pytest
import requests
from faker import Faker

from config.config import url_base, headers
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
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
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.faker = Faker()

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Project")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Edwin Taquichiri")
    def test_create_project(self, test_log_name):
        """
        Test for create a project
        :param test_log_name:  log the test name
        """
        # body
        project_body = {
            "name": f"Project {self.faker.company()}",
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

    @pytest.mark.acceptance
    @allure.title("Test Get Project")
    @allure.tag("acceptance")
    @allure.label("owner", "Edwin Taquichiri")
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

    @pytest.mark.acceptance
    @allure.title("Test Update Project")
    @allure.tag("acceptance")
    @allure.label("owner", "Edwin Taquichiri")
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

    @pytest.mark.acceptance
    @allure.title("Test Delete Project")
    @allure.tag("acceptance")
    @allure.label("owner", "Edwin Taquichiri")
    def test_delete_project(self, create_project, test_log_name):
        """
        Test for delete a project
        :param create_project:  (str) Id of the project
        :param test_log_name:   (str) log the test name
        """
        url_delete_project = f"{url_base}projects/{create_project}"
        LOGGER.debug(f"URL delete project: {url_delete_project}")
        response = self.rest_client.send_request(
            "DELETE", url=url_delete_project, headers=headers
        )

        # assertion
        self.validate.validate_response(response, "delete_project")

    @pytest.mark.functional
    @allure.title("Test validate error message when try to create project without name")
    @allure.tag("functional", "negative")
    @allure.label("owner", "Edwin Taquichiri")
    def test_create_project_without_body_negative(self, test_log_name):
        """
        Test for create project without body
        :param test_log_name:
        """
        # act
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}projects", headers=headers
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        # assertion
        self.validate.validate_response(response, "create_project_without_body")

    @pytest.mark.functional
    @allure.title("Test validate to create project wit different inputs")
    @allure.tag("functional")
    @allure.label("owner", "Edwin Taquichiri")
    @pytest.mark.parametrize(
        "name_project_test", ["12312323", "!@@#$$$%", "<script>alert('test');</script>"]
    )
    def test_create_project_using_different_name_data(
        self, test_log_name, name_project_test
    ):
        """
        Test for create a project using different inputs in project name
        :param test_log_name:  log the test name
        """
        # body
        project_body = {
            "name": f"{name_project_test}",
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
