#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Any, Optional, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator for Cache class """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ increse """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """call_history decorator to store the history of inputs and outputs
    for a particular function."""

    @wraps(method)
    def wrapper(self, *args):
        """ call history"""
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper

def replay(fn: Callable) -> None:
    """  display the history of calls of a particular function.
    """
    if fn is None or not hasattr(fn, '__self__'):
        return
    client = getattr(fn.__self__, '_redis', None)
    if not isinstance(client, redis.Redis):
        return

    calls = client.get(fn.__qualname__).decode('utf-8')

    inputs = client.lrange("{}:inputs".format(fn.__qualname__), 0, -1)
    outputs = client.lrange("{}:outputs".format(fn.__qualname__), 0, -1)

    print(f'{fn.__qualname__} was called {calls} times:')
    for input, output in zip(inputs, outputs):
        print(f"{fn.__qualname__} (*{input.decode('utf-8')}) -> {output.decode('utf-8')}")


class Cache():
    def __init__(self):
        """Initializing class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method
        """
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """get data
        """
        value = self._redis.get(key)
        if fn is int:
            return self.get_int(value)
        elif fn is str:
            return self.get_str(value)
        return value

    def get_str(self, value: bytes) -> str:
        """ get string"""
        return str(value)

    def get_int(self, value: bytes) -> int:
        """"get number"""
        return int(value)
