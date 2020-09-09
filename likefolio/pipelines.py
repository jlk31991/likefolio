# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.utils.project import get_project_settings
settings = get_project_settings

from scrapy.exceptions import DropItem
import logging
from datetime import datetime

class CPIMongoPipeline(object):
    def process_item(self, item, spider):
        return item

class SentimentMongoPipeline(object):
    def process_item(self, item, spider):
        return item

class MentionsMongoPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):

    cpi='cpi'

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls (
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://discoveredlit:discoveredlit@likefolio-k9tqn.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.likefolio2
        self.collection=self.db[self.cpi]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        logging.debug("Post added to MongoDB")
        return item

class MongoDBSentimentPipeline(object):

    sentiment='sentiment'

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls (
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://discoveredlit:discoveredlit@likefolio-k9tqn.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.likefolio2
        self.collection=self.db[self.sentiment]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        logging.debug("Post added to MongoDB")
        return item

class MongoDBMentionsPipeline(object):

    mentions='mentions'

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls (
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_collection=crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://discoveredlit:discoveredlit@likefolio-k9tqn.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.likefolio2
        self.collection=self.db[self.mentions]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        logging.debug("Post added to MongoDB")
        return item
