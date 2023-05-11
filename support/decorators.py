import time


def timer(func):
    """Считает время выполнения функции.
    """
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} выполнилась за {runtime:.10f} секунд")
        return result
    return _wrapper
