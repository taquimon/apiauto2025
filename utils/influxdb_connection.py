import logging
import influxdb_client
import time

from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

from config.config import influxdb_token

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class InfluxDBConnection:
    def __init__(self):
        token = influxdb_token
        print(token)
        org = "berserker"
        url = "http://localhost:8086"

        self.write_client = influxdb_client.InfluxDBClient(
            url=url, token=token, org=org
        )
        self.bucket = "todoapi"
        self.write_api = self.write_client.write_api(write_options=SYNCHRONOUS)

    def store_data_influxdb(self, response, endpoint):
        # response = rest_client.send_request("GET", url=f"{url_base}projects", headers=headers)
        LOGGER.debug("Response Influx %s", response["request"])
        LOGGER.debug(
            "Data store in DB: %s, %s, %s, %s",
            endpoint,
            response["request"].url,
            response["request"].method,
            response["status_code"],
        )
        point = (
            Point("response_time")
            .tag("url", response["request"].url)
            .tag("method", response["request"].method)
            .tag("status", response["status_code"])
            .tag("endpoint", endpoint)
            .field("value", response["time"])
        )
        self.write_api.write(bucket=self.bucket, org="berserker", record=point)
        time.sleep(1)  # separate points by 1 second

    def close(self):
        self.write_client.close()


# query_api = write_client.query_api()
#
# query = """from(bucket: "todoapi")
#  |> range(start: -10m)
#  |> filter(fn: (r) => r._measurement == "response_time")"""
# tables = query_api.query(query, org="berserker")
#
# for table in tables:
#   for record in table.records:
#     print(record)


# query_api = write_client.query_api()
#
# query = """from(bucket: "todoapi")
#   |> range(start: -10m)
#   |> filter(fn: (r) => r._measurement == "measurement1")
#   |> mean()"""
# tables = query_api.query(query, org="berserker")
#
# for table in tables:
#     for record in table.records:
#         print(record)
