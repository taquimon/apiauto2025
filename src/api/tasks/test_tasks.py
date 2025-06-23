import json
import logging

import allure
import requests
from faker import Faker

from config.config import url_base, headers
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


@allure.story("Task")
@allure.parent_suite("Task")
class TestTask:
    @classmethod
    def setup_class(cls):
        """
        Setup before all tests
        :return:
        """
        # Arrange
        cls.task_list = []
        cls.rest_client = RestClient()
        cls.validate = ValidateResponse()
        cls.faker = Faker()

    def test_create_task_without_project_and_section_ids(self, test_log_name):
        # body
        task_body = {
            "content": "Task without project and section ids",
            "description": "Task created for testing purposes",
            "labels": ["API", "Automation", "Test"],
        }
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}tasks", headers=headers, body=task_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        self.task_list.append(response["body"]["id"])
        # assertion
        assert response["status_code"] == 200

    def test_create_task_with_project_and_without_section_id(
        self, test_log_name, create_project
    ):
        """

        :param test_log_name:
        :param create_project:
        :return:
        """

        # body
        task_body = {
            "content": "Task without project and section ids",
            "description": "Task created for testing purposes",
            "project_id": f"{create_project}",
            "labels": ["API", "Automation", "Test project"],
        }
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}tasks", headers=headers, body=task_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        self.task_list.append(response["body"]["id"])
        # assertion
        assert response["status_code"] == 200

    def test_create_task_with_project_and_section_ids(
        self, test_log_name, create_project, create_section
    ):
        """

        :param test_log_name:
        :param create_project:
        :return:
        """

        # body
        task_body = {
            "content": "Task without project and section ids",
            "description": "Task created for testing purposes",
            "project_id": f"{create_project}",
            "section_id": f"{create_section}",
            "labels": ["API", "Automation", "Test Section"],
        }
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST", url=f"{url_base}tasks", headers=headers, body=task_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        self.task_list.append(response["body"]["id"])
        # assertion
        assert response["status_code"] == 200

    def test_get_task(self, test_log_name, create_task):
        """

        :param test_log_name:
        :param create_task:
        :return:
        """
        url_get_task = f"{url_base}tasks/{create_task}"
        response = self.rest_client.send_request(
            "GET",
            url=url_get_task,
            headers=headers,
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        self.task_list.append(response["body"]["id"])
        # assertion
        assert response["status_code"] == 200

    def test_delete_task(self, test_log_name, create_task):
        """

        :param test_log_name:
        :param create_task:
        :return:
        """
        url_delete_task = f"{url_base}tasks/{create_task}"
        response = self.rest_client.send_request(
            "DELETE",
            url=url_delete_task,
            headers=headers,
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        # assertion
        assert response["status_code"] == 204

    def test_update_task(self, test_log_name, create_task):
        """

        :param test_log_name:
        :param create_task:
        """

        # body
        task_body = {
            "content": "Task updated",
            "description": "Task created for testing purposes",
            "labels": ["API Updated", "Automation Updated", "Test Updated"],
        }
        url_task_update = f"{url_base}tasks/{create_task}"
        # call endpoint using requests
        response = self.rest_client.send_request(
            "POST", url=url_task_update, headers=headers, body=task_body
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))
        # assertion
        self.task_list.append(response["body"]["id"])
        # assertion
        assert response["status_code"] == 200

    def test_close_task(self, test_log_name, create_task):
        """

        :param test_log_name:
        :param create_task:
        :return:
        """
        url_close_task = f"{url_base}tasks/{create_task}/close"
        response = self.rest_client.send_request(
            "POST",
            url=url_close_task,
            headers=headers,
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        # assertion
        assert response["status_code"] == 204

    def test_reopen_task(self, test_log_name, create_task):
        """
        Test to reopen a task
        :param test_log_name:
        :param create_task:
        :return:
        """
        url_reopen_task = f"{url_base}tasks/{create_task}/reopen"
        response = self.rest_client.send_request(
            "POST",
            url=url_reopen_task,
            headers=headers,
        )
        LOGGER.debug("Response: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("Status Code: %s", str(response["status_code"]))

        # assertion
        assert response["status_code"] == 204

    def test_move_task(
        self, test_log_name, create_task, create_project, create_section
    ):
        body_move_task = {
            "project_id": f"{create_project}",
            "section_id": f"{create_section}",
        }
        url_reopen_task = f"{url_base}tasks/{create_task}/move"
        response = self.rest_client.send_request(
            "POST", url=url_reopen_task, headers=headers, body=body_move_task
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
        LOGGER.info("Test Task teardown Class")
        for task_id in cls.task_list:
            url_delete_task = f"{url_base}tasks/{task_id}"
            LOGGER.debug(f"URL delete task: {url_delete_task}")
            response = requests.delete(url=url_delete_task, headers=headers)
            LOGGER.debug("Status Code: %s", str(response.status_code))
            if response.status_code == 204:
                LOGGER.debug("task deleted")
