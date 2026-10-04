from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        else:
            print("Calculating new result")
            stored_results[args] = func(*args, **kwargs)
            return stored_results[args]
    return wrapper
