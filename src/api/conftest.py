import json
import logging
import pytest

import requests

from config.config import headers, url_base
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


# Arrange
@pytest.fixture
def create_project():
    LOGGER.info("create project fixture")
    # project body
    project_body = {
        "name": "Test Project from fixture",
    }
    # call endpoint using requests
    response = requests.post(
        url=f"{url_base}projects", headers=headers, json=project_body
    )
    LOGGER.debug(json.dumps(response.json(), indent=4))

    # get id project
    project_id = response.json()["id"]
    # once the test ends yield call to delete the project
    yield project_id
    delete_project(project_id)


# Arrange
@pytest.fixture
def test_log_name(request):
    LOGGER.info(f"Start test '{request.node.name}'")

    def fin():
        LOGGER.info(f"End test '{request.node.name}'")

    request.addfinalizer(fin)


def delete_project(project_id):
    LOGGER.info("Delete project fixture (yield)")
    url_delete_project = f"{url_base}projects/{project_id}"
    LOGGER.debug(f"URL delete project fixture: {url_delete_project}")
    response = requests.delete(url=url_delete_project, headers=headers)
    # LOGGER.debug("Response: %s", response.json())
    LOGGER.debug("Status Code: %s", str(response.status_code))
    if response.status_code == 204:
        LOGGER.debug("Project deleted")


@pytest.fixture()
def create_section(create_project):
    LOGGER.debug("Create section fixture")

    body_section = {"project_id": f"{create_project}", "name": "Section from fixture"}
    url_section = f"{url_base}sections"
    response = requests.post(url_section, json=body_section, headers=headers)
    LOGGER.debug("Response Section: %s", str(response.json()))
    section_id = response.json()["id"]
    yield section_id


@pytest.fixture()
def create_task():
    LOGGER.debug("Create task fixture")

    task_body = {
        "content": "Task without project and section ids",
        "description": "Task created for testing purposes",
        "labels": ["API", "Automation", "Test"],
    }
    url_task = f"{url_base}tasks"
    response = requests.post(url_task, json=task_body, headers=headers)
    LOGGER.debug("Response Section: %s", str(response.json()))
    task_id = response.json()["id"]
    yield task_id


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment where the tests are executed",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        help="Browser where the UI tests are executed",
    )
