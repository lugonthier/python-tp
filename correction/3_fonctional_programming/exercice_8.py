import time
from functools import wraps
import time
from functools import wraps
import logging

def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} a pris {end - start:.4f} secondes")
        return result
    return wrapper

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        log = logging.getLogger(func.__name__)
        
        log.info(f"Calling function with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)
            

        log.info(f"Successfully returned: {result}")
        return result

            
    return wrapper


@logger
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))