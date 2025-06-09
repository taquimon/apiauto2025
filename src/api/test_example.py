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
            LOGGER.info('Setup class')

        def test_one(self):
            LOGGER.info('Test one')

        def test_two(self):
            LOGGER.info('Test two')

        def test_three(self):
            LOGGER.info('Test three')

        @classmethod
        def teardown_class(cls):
            LOGGER.info('Teardown class')
