"""
Unfinished thingy, but it runs and does something. At least on
a Ubuntu sytem.
"""

import multiprocessing
import concurrent.futures
import typing
import message_bridge
import logging


logger = None


def start_bridge(config: list,
                 on_shutdown: typing.Callable[[], None],
                 reconnect_enable: bool = True):
    futures = list()
    threads = list()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(config)) as executor:
        for bridge_config in config:
            bridge = message_bridge.MessageBridge(
                bridge_config, reconnect_enable)
            threads.append(bridge)
            futures.append(executor.submit(bridge.run))

        concurrent.futures.wait(futures, timeout=None, return_when=concurrent.futures.FIRST_COMPLETED)

def bridge_process(configuration: list,
                   on_shutdown: typing.Callable[[], None],
                   on_finished: typing.Callable[[], None],
                   reconnect_enable: bool = True):
    try:
        start_bridge(configuration, on_shutdown, reconnect_enable)
    finally:
        logger.info('finally block')
        on_shutdown()
        #on_finished()

def start(config: dict, reconnect_enable: bool = True):
    logger.info('start method: Starting')
    shuting_down = multiprocessing.Event()
    finished = multiprocessing.Event()

    process = multiprocessing.Process(
        target = bridge_process,
        args=(config, lambda: shuting_down.set(), lambda: finished.set(), reconnect_enable)
    )
    process.start()

    shuting_down.wait()

    logger.info("Shuting down")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(name)s %(funcName)s %(lineno)d %(message)s')
    logger = logging.getLogger(__name__)
    config =['bridge-1', 'bridge-2', 'bridge-3']
    start(config)
