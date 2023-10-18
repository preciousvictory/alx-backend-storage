#!/usr/bin/env python3
""" 10-update_topics
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """update_topics
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}});
