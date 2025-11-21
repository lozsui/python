import logging
import threading
import time


def worker(arg, worker_name):
    while not arg["stop"]:
        logging.debug("Hi from myfunc", extra={"context": worker_name})
        time.sleep(1)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="|%(name)s | %(relativeCreated)6d | %(threadName)s | %(message)s| %(context)s",
    )
    info = {"stop": False}
    thread = threading.Thread(target=worker, args=(info, "guardian-of-house"))
    thread.start()
    while True:
        try:
            logging.debug("Hello from main", extra={"context": "MAIN-THREAD"})
            time.sleep(3)
        except KeyboardInterrupt:
            info["stop"] = True
            break
    thread.join()


if __name__ == "__main__":
    main()
