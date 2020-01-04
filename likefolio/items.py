# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LikefolioItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # cpi = scrapy.Field()
    # sentiment = scrapy.Field()
    # mentions = scrapy.Field()
    data = scrapy.Field()

# date = scrapy.Field()
# value = scrapy.Field()
# price = scrapy.Field()

