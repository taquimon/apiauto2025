import json
import logging

from helper.rest_client import RestClient
from utils.logger import get_logger

from behave import when, then

LOGGER = get_logger(__name__, logging.DEBUG)

rest_client = RestClient()


@when('user calls "{method}" method to "{endpoint_name}" endpoint')
def call_endpoints(context, method, endpoint_name):
    LOGGER.debug("Step %s using %s method", endpoint_name, method)
    url_get_project = f"{context.url_base}projects/{context.project_id}"
    response = rest_client.send_request(
        method, url=url_get_project, headers=context.headers
    )
    LOGGER.debug(response)
    # store status code in context
    context.status_code = response["status_code"]


@when('user calls "{method}" method to "{endpoint_name}" endpoint using json')
def call_endpoints_with_json(context, method, endpoint_name):
    LOGGER.debug("JSON: %s", context.text)
    LOGGER.debug("Step %s using %s method", endpoint_name, method)
    url_create_project = f"{context.url_base}projects"
    if "update" in endpoint_name:
        url_create_project = f"{context.url_base}projects/{context.project_id}"
    body = json.loads(context.text)

    response = rest_client.send_request(
        method, url=url_create_project, headers=context.headers, body=body
    )
    # add to list of projects for clean up
    if "update" not in endpoint_name:
        context.project_list.append(response["body"]["id"])
    LOGGER.debug(response)
    # store status code in context
    context.status_code = response["status_code"]


@then("the status code is {status_code:d}")
def verify_status_code(context, status_code):
    LOGGER.debug("Step verify status code %s", status_code)
    assert context.status_code == status_code
