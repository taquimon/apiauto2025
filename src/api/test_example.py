import logging
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)

class TestExample:

        @classmethod
        def setup_class(cls):
            """
            Setup class
            :return:
            """
            # Arrange (Initial data)
            API_KEY = ""
            LOGGER.info("Setup class")
            cls.header_api = {
                "Authorization": "Bearer {}".format(API_KEY),
            }
            LOGGER.debug("HEADER API: %s", cls.header_api)


        def test_one(self):
            # act (test)
            LOGGER.info('Test one: %s', self.header_api)
            # assert (validation)
            assert self.header_api

        def test_two(self):
            LOGGER.info("Test two %s", self.header_api)


        def test_three(self):
            LOGGER.info('Test three')

        def teardown_method(self):
            # clean up (delete data)
            LOGGER.info('teardown method')

        @classmethod
        def teardown_class(cls):
            # clean up (delete data)
            LOGGER.info('Teardown class')

        def setup_method(self):
            LOGGER.info('Setup method')
