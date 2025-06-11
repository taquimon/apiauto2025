import logging
import pytest
import os

import requests

from utils.logger import get_logger
from dotenv import load_dotenv

LOGGER = get_logger(__name__, logging.DEBUG)
# Arrange
@pytest.fixture(scope='class', name='config')
def first_entry(request):
    environment  = request.config.getoption('--env')
    browser = request.config.getoption('--browser')

    # Get the secret key from the environment
    secret_key = os.environ.get('token')
    LOGGER.debug(secret_key)

    # get secrets using dotenv
    load_dotenv()
    api_token = os.getenv("TOKEN_TODO")
    LOGGER.debug("API Token todo: %s", api_token)
    url_base = os.getenv("URL_BASE")
    LOGGER.debug("URL base: %s", url_base)

    LOGGER.warning("Environment, %s", environment)
    LOGGER.warning("Browser, %s", browser)
    return "a"

# Arrange
@pytest.fixture
def order(config):
    LOGGER.warning("order fixture")
    return config

@pytest.fixture(scope='class')
def get_data_api():
    LOGGER.warning("get headers")
    api_data = {}
    load_dotenv()
    api_token = os.getenv("TOKEN_TODO")
    url_base = os.getenv("URL_BASE")

    headers = {
        "Authorization": "Bearer {}".format(api_token),
    }
    api_data['headers'] = headers
    api_data['url_base'] = url_base

    return api_data

@pytest.fixture
def create_project(get_data_api):
    # headers
    # body
    project_body = {
        "name": "Test Project from fixture",
    }

    # call endpoint using requests
    url_base = os.getenv("URL_BASE")
    response = requests.post(url=f"{url_base}projects", headers=get_data_api['headers'], json=project_body)
    LOGGER.debug(response.json())

    # get id project
    project_id = response.json()["id"]

    # return id
    return project_id

def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='dev', help="Environment where the tests are executed"
    )
    parser.addoption(
        '--browser', action='store', default='edge', help="Browser where the UI tests are executed"
    )
