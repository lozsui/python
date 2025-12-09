import os
import time


def watch_files(path):
    while True:
        if os.listdir(path):
            print(f"found file at {path}")
        time.sleep(10)


if __name__ == "__main__":
    watch_files("files")
