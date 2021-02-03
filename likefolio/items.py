# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#added this 20200827
from scrapy.item import Item, Field

class CPIMongoItem(scrapy.Item):
    # define the fields for your item here like:

    date = scrapy.Field()
    value = scrapy.Field()
    internalName = scrapy.Field()
    name = scrapy.Field()
    total = scrapy.Field()
    change = scrapy.Field()
    frequency = scrapy.Field()
    expectations = scrapy.Field()
    visualizationType = scrapy.Field()
    visualizationData = scrapy.Field()
    topic = scrapy.Field()

    pass

class SentimentMongoItem(scrapy.Item):
    date = scrapy.Field()
    positive = scrapy.Field()
    negative = scrapy.Field()
    internalName = scrapy.Field()
    name = scrapy.Field()
    total = scrapy.Field()
    change = scrapy.Field()
    frequency = scrapy.Field()
    expectations = scrapy.Field()
    visualizationType = scrapy.Field()
    visualizationData = scrapy.Field()
    topic = scrapy.Field()

    pass

class MentionsMongoItem(scrapy.Item):
    date = scrapy.Field()
    value = scrapy.Field()
    internalName= scrapy.Field()
    name = scrapy.Field()
    total = scrapy.Field()
    change = scrapy.Field()
    frequency = scrapy.Field()
    expectations = scrapy.Field()
    visualizationType = scrapy.Field()
    visualizationData = scrapy.Field()
    topic = scrapy.Field()
    
    pass