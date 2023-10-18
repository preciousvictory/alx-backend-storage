#!/usr/bin/env python3
"""
exercise file
"""
import redis
import uuid
from typing import Any


class Cache():
    def __init__(self):
        """Initializing class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """store method
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
