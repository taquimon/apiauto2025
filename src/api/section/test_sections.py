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


@allure.story("Section")
@allure.parent_suite("Section")
class TestSection:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.section_list = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.faker = Faker()

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Section")
    @allure.tag("acceptance", "smoke")
    @allure.label("owner", "Edwin Taquichiri")
    def test_create_section(self, test_log_name, create_project):
        """
        Test for create a Section
        :param test_log_name:  log the test name
        """
        # body
        section_body = {
            "project_id": f"{create_project}",
            "name": f"Section {self.faker.company()}",
        }
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}sections", headers=headers, body=section_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        self.section_list.append(response["body"]["id"])
        # assertion
        assert response["status_code"] == 200

    @pytest.mark.acceptance
    @allure.title("Test Get Section")
    @allure.tag("acceptance")
    @allure.label("owner", "Edwin Taquichiri")
    def test_get_section(self, create_section, test_log_name):
        """
        Test for get a Section
        :param create_section:   (str) Id of the Section
        :param test_log_name:    (str) log the test name
        """
        # url for get the Section
        url_get_section = f"{url_base}sections/{create_section}"
        LOGGER.debug(f"URL get Section: {url_get_section}")

        # call GET endpoint (act)
        response = self.rest_client.send_request(
            "GET", url=url_get_section, headers=headers
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        assert response["status_code"] == 200

    @pytest.mark.acceptance
    @allure.title("Test Update Section")
    @allure.tag("acceptance")
    @allure.label("owner", "Edwin Taquichiri")
    def test_update_section(self, create_section, test_log_name):
        """
        Test for update a Section
        :param create_section: (str) Id of the Section
        :param test_log_name:  (str) log the test name
        """
        # url for update the Section
        url_update_section = f"{url_base}sections/{create_section}"
        # boy for update Section
        update_section_body = {
            "name": "Updated Section",
            "description": "Section description updated",
            "color": "yellow",
        }
        LOGGER.debug(f"URL update Section: {url_update_section}")
        # call POST endpoint
        response = self.rest_client.send_request(
            "POST", url=url_update_section, headers=headers, body=update_section_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        assert response["status_code"] == 200

    @pytest.mark.acceptance
    @allure.title("Test Delete Section")
    @allure.tag("acceptance")
    @allure.label("owner", "Edwin Taquichiri")
    def test_delete_section(self, create_section, test_log_name):
        """
        Test for delete a Section
        :param create_section:  (str) Id of the Section
        :param test_log_name:   (str) log the test name
        """
        url_delete_section = f"{url_base}sections/{create_section}"
        LOGGER.debug(f"URL delete Section: {url_delete_section}")
        response = self.rest_client.send_request(
            "DELETE", url=url_delete_section, headers=headers
        )

        # assertion
        self.validate.validate_response(response, "delete_section")

    @pytest.mark.functional
    @allure.title("Test validate error message when try to create Section without name")
    @allure.tag("functional", "negative")
    @allure.label("owner", "Edwin Taquichiri")
    def test_create_section_without_body_negative(self, test_log_name):
        """
        Test for create a section without body
        :param test_log_name:
        """
        # act
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}Sections", headers=headers
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        # assertion
        self.validate.validate_response(response, "create_section_without_body")

    @pytest.mark.functional
    @allure.title("Test validate to create section wit different inputs")
    @allure.tag("functional")
    @allure.label("owner", "Edwin Taquichiri")
    @pytest.mark.parametrize(
        "name_section_test", ["12312323", "!@@#$$$%", "<script>alert('test');</script>"]
    )
    def test_create_section_using_different_name_data(
        self, test_log_name, name_section_test, create_project
    ):
        """
        Test for create a Section using different inputs in Section name
        :param test_log_name:  log the test name
        """
        # body
        section_body = {
            "project_id": f"{create_project}",
            "name": f"{name_section_test}",
        }
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}sections", headers=headers, body=section_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        assert response["status_code"] == 200

    @classmethod
    def teardown_class(cls):
        """
        Clean up after all tests
        :return:
        """
        # Cleanup Sections
        LOGGER.info("Test Section teardown Class")
        for section_id in cls.section_list:
            url_delete_section = f"{url_base}sections/{section_id}"
            LOGGER.debug(f"URL delete Section: {url_delete_section}")
            response = requests.delete(url=url_delete_section, headers=headers)
            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 204:
                LOGGER.debug("Section deleted")
