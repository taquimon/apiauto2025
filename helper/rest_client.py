import requests
import logging
from utils.logger import get_logger
from utils.singleton import Singleton

LOGGER = get_logger(__name__, logging.DEBUG)


class RestClient(metaclass=Singleton):
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method_name, url, headers=None, body=None, data=None):
        response_updated = {}
        methods = {
            "GET": self.session.get,
            "POST": self.session.post,
            "DELETE": self.session.delete,
        }

        try:
            # response = requests.post(url=f"{url_base}projects", headers=headers, json=project_body)

            response = methods[method_name](
                url=url, headers=headers, json=body, data=data
            )
            response.raise_for_status()
            response_updated["body"] = (
                response.json() if response.text else {"message": "No body content"}
            )
            response_updated["status_code"] = response.status_code
            response_updated["headers"] = dict(response.headers)
            response_updated["time"] = response.elapsed.total_seconds()
            response_updated["request"] = response.request

        except requests.exceptions.HTTPError as e:
            LOGGER.error("HTTP Error: %s", e)
            response_updated["body"] = (
                response.json() if response.text else {"message": "HTTP error"}
            )
            response_updated["status_code"] = response.status_code
            response_updated["headers"] = dict(response.headers)
            response_updated["time"] = response.elapsed.total_seconds()
            response_updated["request"] = response.request

        except requests.exceptions.ConnectionError as e:
            LOGGER.error("Connection Error: %s" % e)
            response_updated["body"] = (
                response.json() if response.text else {"message": "Connection Error"}
            )
            response_updated["status_code"] = response.status_code
            response_updated["headers"] = {}

        except requests.exceptions.RequestException as e:
            LOGGER.error("Request Exception: %s" % e)
            response_updated["body"] = (
                response.json() if response.text else {"message": "Request Failed"}
            )
            response_updated["status_code"] = response.status_code
            response_updated["headers"] = {}
            response_updated["time"] = response.elapsed.total_seconds()
            response_updated["request"] = response.request

        return response_updated
