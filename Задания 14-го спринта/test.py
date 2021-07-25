import time
from functools import wraps


def hash_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        pre_result = func(*args, **kwargs)
        end = time.time()
        result = {pre_result[0], pre_result[1:]}
        print(end - start)
        return result
    return wrapper


@hash_function
def index(n: list):
    return len(n), *n


if __name__ == '__main__':
    n = [i for i in range(8)]
    print(index(n))
