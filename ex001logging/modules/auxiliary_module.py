import logging

# create logger
module_logger = logging.getLogger("spam_application.auxiliary")


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger("spam_application.auxiliary.Auxiliary")
        self.logger.info("creating an instance of Auxiliary")

    def do_something(self):
        self.logger.info("doing something")
        a = 1 + 1
        self.logger.info(f"done doing something (1 + 1) equals {a}")


def some_function():
    module_logger.info('received a call to "some_function"')
