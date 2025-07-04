import json
import logging

from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from utils.logger import get_logger

from behave import when, then, step

LOGGER = get_logger(__name__, logging.DEBUG)

rest_client = RestClient()
validator = ValidateResponse()


@when('user calls "{method}" method to "{action}" "{endpoint_name}" endpoint')
def call_endpoints(context, method, action, endpoint_name):
    LOGGER.debug("Step %s using %s method", endpoint_name, method)
    feature_id = get_feature_id(endpoint_name, context)
    url_get_project = f"{context.url_base}{endpoint_name}/{feature_id}"
    response = rest_client.send_request(
        method, url=url_get_project, headers=context.headers
    )
    LOGGER.debug(response)
    # store status code in context
    context.status_code = response["status_code"]


@when(
    'user calls "{method}" method to "{action}" "{endpoint_name}" endpoint using json'
)
def call_endpoints_with_json(context, method, action, endpoint_name):
    LOGGER.debug("JSON: %s", context.text)
    LOGGER.debug("Step %s using %s method", endpoint_name, method)
    url_create_feature = f"{context.url_base}{endpoint_name}"
    if action == "update":
        feature_id = get_feature_id(endpoint_name, context)
        url_create_feature = f"{context.url_base}{endpoint_name}/{feature_id}"
    body = json.loads(context.text)

    body_updated = update_json_data(context, body)

    response = rest_client.send_request(
        method, url=url_create_feature, headers=context.headers, body=body_updated
    )
    # add to list of projects for clean up
    LOGGER.debug("Response %s", response)
    if action == "create" and "id" in response["body"]:
        append_to_feature_list(endpoint_name, context, response["body"]["id"])
    LOGGER.debug(response)
    # store status code in context
    context.status_code = response["status_code"]
    context.response = response


@then("the status code is {status_code:d}")
def verify_status_code(context, status_code):
    LOGGER.debug("Step verify status code %s", status_code)
    assert context.status_code == status_code


@step('the response is validated with "{json_file}" file')
def validate_json(context, json_file):
    validator.validate_response(context.response, json_file)


def get_feature_id(endpoint_name, context):
    LOGGER.debug("Feature id %s", endpoint_name)
    feature_id = None
    if endpoint_name == "projects":
        feature_id = context.project_id
    elif endpoint_name == "sections":
        feature_id = context.section_id
    elif endpoint_name == "tasks":
        feature_id = context.task_id
    return feature_id


def append_to_feature_list(endpoint_name, context, feature_id):
    if endpoint_name == "projects":
        context.project_list.append(feature_id)
    elif endpoint_name == "sections":
        context.section_list.append(feature_id)


def update_json_data(context, body):
    keys = ["project_id", "section_id", "task_id"]
    """
    {
      "project_id": "project_id"
      "name": "Section from feature file"
    }
    context = {
        "project_id": "12123siujdi",
        "project_list": ["..."]
    }
    """
    LOGGER.debug("Method update json data")
    for key in keys:
        for d in body.keys():
            if d == key and hasattr(context, key):
                body[d] = getattr(context, key)
                LOGGER.debug("Key changed %s", d)

    LOGGER.debug("Update body %s", body)

    return body
