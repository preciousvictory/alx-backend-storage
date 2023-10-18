#!/usr/bin/env python3
"""-insert_school
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """insert_school
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
