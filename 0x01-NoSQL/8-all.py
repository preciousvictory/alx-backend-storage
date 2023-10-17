#!/usr/bin/env python3
"""8-all
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """list_all
    """
    return mongo_collection.find()
