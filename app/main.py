from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_results = {}
    stored_results[func] = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in stored_results[func]:
            print("Getting from cache")
            return stored_results[func][key]
        else:
            print("Calculating new result")
            stored_results[func][key] = func(*args, **kwargs)
            return stored_results[func][key]
    return wrapper
