import logging

"""
https://docs.python.org/3/tutorial/errors.html is your friend.
"""


def example_2():
    logging.warning(">>> Example 2: Find out what kind of error is risen.")
    try:
        logging.warning(inexistent_var)
    except Exception as error:
        logging.warning(f"Unexpected {error=}, {type(error)=}")


def example_1():
    logging.warning(">>> Example 1: Exception has tuple of 'args'")
    try:
        logging.warning(inexistent_var)
    except Exception as e:
        logging.warning(f"There are {len(e.args)} args in Exception e.")
        logging.warning(f"Type of e.args is {type(e.args)}.")
        for arg in e.args:
            logging.warning(f"{arg}")
        raise


examples = [
    # example_1,
    example_2,
]

if __name__ == "__main__":
    for example in examples:
        example()
