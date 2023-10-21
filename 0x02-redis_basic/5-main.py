#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page
redis =  __import__('web').client


url = 'http://slowwly.robertomurray.co.uk'

get_page(url)
print(redis.get(f'count:{url}'))
print(redis.ttl(f'result:{url}'))
