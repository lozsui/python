import threading
import time
import logging
import random


class MessageBridge(threading.Thread):

    def __init__(self, name, reconnect_enable: bool):
        super().__init__(daemon=True, name=name)
        self.name = name
        self.reconnect_enable = reconnect_enable
        logging.basicConfig(level=logging.INFO, format='%(name)s %(funcName)s %(lineno)d %(message)s')
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info(f'Started {self.name}')
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
        self.logger.info(f'{self.name} slept for {sleep_time} seconds.')

    def stop(self):
        self.logger.info(f'{self.name} hit stop method')
