#!/usr/bin/env python3
""" 11-schools_by_topic
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """mongo_collection
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return  [doc for doc in mongo_collection.find(topic_filter)]
