#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Any, Optional, Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ increse """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache():
    def __init__(self):
        """Initializing class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, int, bytes, float]) -> str:
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
