import requests


class RestClient:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method_name, url, headers, body):
        response_updated = {}
        methods = {
            "GET": self.session.get,
            "POST": self.session.post,
            "DELETE": self.session.delete,
        }

        try:
            # response = requests.post(url=f"{url_base}projects", headers=headers, json=project_body)
            response_updated = methods[method_name](url, headers=headers, json=body)
            response = methods[method_name](url=url, headers=headers, json=body)
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            print("Error: %s" % e)
        except requests.exceptions.ConnectionError as e:
            print("Error: %s" % e)
        # LOGGER.debug("")
        # add headers, response empty, headers request

        return response_updated
