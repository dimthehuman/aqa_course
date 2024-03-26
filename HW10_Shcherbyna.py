import time


# Task 1
def time_decorator(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} function execution time: {end_time - start_time}")
        return result
    return wrap


# Task 2
def logger_decorator(text):
    def sub_logger_decorator(func):
        def wrap(*args, **kwargs):
            print(text)
            result = func(*args, **kwargs)
            return result
        return wrap
    return sub_logger_decorator
