import multiprocessing


def bridge_process(config, shutdown_callback, finish_callback, reconnect_enable):
    print(f'config: {config}')
    print('shutdown_callback')
    print('finish_callback')
    print(f'reconnect_enable {reconnect_enable}')

def start(config: dict, reconnect_enable: bool = True):
    
    # logging.info('Start adapter')
    shuting_down = multiprocessing.Event()
    finished = multiprocessing.Event()

    process = multiprocessing.Process(
        target = bridge_process,
        args=(config, lambda: shuting_down.set(), lambda: finished.set(), reconnect_enable)
    )
    process.start()

    shuting_down.wait()

    # logging.info("Shuting down")

if __name__ == "__main__":
    config = {'process_time': 10}
    start(config)
