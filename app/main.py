from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}
    stored_results[func] = {}
    def wrapper(*args, **kwargs) -> Any:
        if args in stored_results[func]:
            print("Getting from cache")
            return stored_results[func][args]
        else:
            print("Calculating new result")
            stored_results[func][args] = func(*args, **kwargs)
            return stored_results[func][args]
    return wrapper
