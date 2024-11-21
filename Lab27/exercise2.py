
from datetime import datetime
from functools import lru_cache, wraps


def log_time(func):
    # @wraps(func)
    def wrapper(*args):
        entry = datetime.now()
        print(f'Entry time of', func.__name__,':',entry)
        res = func(*args)
        exit = datetime.now()
        print(f'Exit time of', func.__name__,':', exit)
        print(f'Total time:', entry-exit)
        return res
    return wrapper


@log_time
@lru_cache(maxsize=5)
def fibonacci(n):
    """This function outputs the sum of  n Fibonacci numbers"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
print(f'Docstring output:',fibonacci.__doc__)