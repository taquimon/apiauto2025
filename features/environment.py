import logging

from helper.rest_client import RestClient
from utils.logger import get_logger
from config.config import url_base, headers

LOGGER = get_logger(__name__, logging.DEBUG)


def before_all(context):
    """
     Setup before all Features.
    :param context:  Object  stores test data
    """

    LOGGER.debug("Before all tests")
    context.headers = headers
    context.url_base = url_base
    context.rest_client = RestClient()
    context.project_list = []


def before_feature(context, feature):
    """
    Setup before feature.
    :param context:
    :param feature:
    :return:
    """
    LOGGER.debug("Before feature")


def before_scenario(context, scenario):
    """
    Setup before scenario.
    :param context:
    :param scenario:
    """
    LOGGER.debug('Starting scenario: "%s"', scenario.name)

    # create a project
    LOGGER.debug("SCENARIO TAGS %s", scenario.tags)
    if "project_id" in scenario.tags:
        project_body = {
            "name": "Project before scenario",
        }
        LOGGER.debug("create project")
        response = context.rest_client.send_request(
            "POST",
            url=f"{context.url_base}projects",
            headers=context.headers,
            body=project_body,
        )
        context.project_id = response["body"]["id"]
        context.project_list.append(context.project_id)
        LOGGER.debug("Project ID: %s", response["body"]["id"])


def after_scenario(context, scenario):
    """
    Tear down after the scenario.
    :param context:
    :param scenario:
    :return:
    """
    LOGGER.debug('Ending scenario: "%s"', scenario.name)


def after_feature(context, feature):
    """
    Tear down after feature.
    :param context:
    :param feature:
    :return:
    """
    LOGGER.debug("After feature")


def after_all(context):
    """
    Tear down after all.
    :param context:
    :return:
    """
    LOGGER.debug("After all")
    for project_id in context.project_list:
        url_delete_project = f"{context.url_base}projects/{project_id}"
        response = context.rest_client.send_request(
            "DELETE", url=url_delete_project, headers=context.headers
        )
        if response["status_code"] == 204:
            LOGGER.debug("Project %s deleted", project_id)
