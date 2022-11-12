import time

from logs.settings import logger


def sleep(timeout):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):

            function(*args, **kwargs)
            logger.debug(f'await 10 minutes')
            time.sleep(timeout)

        return wrapper

    return the_real_decorator
