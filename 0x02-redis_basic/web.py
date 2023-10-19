#!/usr/bin/env python3
""" web file"""
import redis
import requests
from typing import Callable
from functools import wraps


def cache(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def wrapper(url: str) -> str:
        '''The wrapper function for caching the output.
        '''
        client = redis.Redis()
        client.incr(f'count:{url}')
        result = client.get(f'result:{url}')
        if result:
            return result.decode('utf-8')

        resp = method(url)
        client.set(f'{url}', resp, 10)
        return resp
    return wrapper

@cache
def get_page(url: str) -> str:
    """uses the requests module to obtain the HTML content of a particular URL and returns it.
    """
    return requests.get(url).text
