import time

from logs.settings import logger
from config import TIME


def sleep(timeout):
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):

            function(*args, **kwargs)
            logger.debug(f'await {TIME / 60} minutes')
            time.sleep(timeout)

        return wrapper

    return the_real_decorator


def retry(timeout=60, attempt=3):
    def the_real_decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < attempt:
                try:
                    value = func(*args, **kwargs)
                    return value
                except Exception as e:
                    logger.error(f'Error: {e}')
                    logger.error(f'Sleep: {timeout} seconds')
                    time.sleep(timeout)
                    attempts += 1
        return wrapper
    return the_real_decorator
