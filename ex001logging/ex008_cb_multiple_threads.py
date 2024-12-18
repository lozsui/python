import logging
import threading
import time


def worker(arg):
    while not arg["stop"]:
        logging.debug("Hi from myfunc")
        time.sleep(1)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(name)s %(relativeCreated)6d %(threadName)s %(message)s",
    )
    info = {"stop": False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug("Hello from main")
            time.sleep(3)
        except KeyboardInterrupt:
            info["stop"] = True
            break
    thread.join()


if __name__ == "__main__":
    main()
