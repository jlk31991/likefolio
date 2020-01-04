import scrapy
import json
import logging

from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, SelectJmes

from likefolio.items import LikefolioItem


class CPISpider(Spider):
    name = "likefolio_to_mongo"
    allowed_domains = ["dashboard.likefolio.com"]
    start_urls = ["https://dashboard.likefolio.com/users/sign_in"]

    cpi_paths = {"date": "start_date", "value": "value", "price": "price"}

    def parse(self, response):
        token = response.xpath('//*[@name="authenticity_token"]/@value').extract_first()
        return FormRequest.from_response(
            response,
            formdata={
                "authenticity_token": token,
                "user[email]": "tonymoo90@gmail.com",
                "user[password]": "discoveredlit",
            },
            callback=self.navigate,
        )

    def navigate(self, response):
        baseurl = "https://dashboard.likefolio.com/"
        pagelist = {
            # "companies/1986/daily_pi.json?apply_corrections=yes&avg_size=90&display_avg=yes&display_daily=no&display_price=yes&period=all&show_annotations=no",
            # "companies/1986/daily_sentiment.json?apply_corrections=yes&avg_size=90&display_avg=yes&display_daily=no&display_price=yes&period=all&show_annotations=no",
            # "companies/1986/daily_mentions.json?apply_corrections=yes&avg_size=90&display_avg=yes&display_daily=no&display_price=yes&period=all&show_annotations=no",
            "companies/1986/daily"
        }
        for page in pagelist:
            # print(page)
            yield Request(url=baseurl + page, callback=self.scrape_pages)

    def scrape_pages(self, response):
        #        open_in_browser(response)
        # logging.error("response", response)
        # print(response)
        item = LikefolioItem()
        item["data"] = response.xpath("/html/body/pre/text()[1]").get()
        # item["data"] = response.xpath(
        #    "/html/body/div[4]/div/div/div[2]/div[1]/h4/span[2]"
        # )
        yield item
        # jsonresponse = json.loads(response.body_as_unicode())

        # for user in jsonresponse:
        # loader = ItemLoader(item=LikefolioItem())
        # loader.deafult_input_processor = MapCompose(str)
        # loader.default_output_processor = Join(" ")

        # for (field, path) in self.cpi_paths.items():
        #    loader.add_value(field, SelectJmes(path)(user))

        # yield loader.load_item


# EXAMPLE OF USING ITEMS
#    def parse(self, response):
#        questions = Selector(response).xpath('//div[@class="summary"]/h3')
#
#        for question in questions:
#            item = StackItem()
#            item['title'] = question.xpath(
#                'a[@class="question-hyperlink"]/text()').extract()[0]
#            item['url'] = question.xpath(
#                'a[@class="question-hyperlink"]/@href').extract()[0]
#           yield item
