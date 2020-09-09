from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from scrapy import Request
from scrapy.spiders.init import InitSpider


class CPISpider(Spider):
    name = "cpi"
    allowed_domains = ["dashboard.likefolio.com"]
    start_urls = ["https://dashboard.likefolio.com/users/sign_in"]

    def parse(self, response):
        token = response.xpath('//*[@name="authenticity_token"]/@value').extract_first()
        return FormRequest.from_response(
            response,
            formdata={
                "authenticity_token": token,
                "user[email]": "tonymoo90@gmail.com",
                "user[password]": "discoveredlit",
            },
            #            callback=self.after_login,
            callback=self.scrape_pages,
        )

    def scrape_pages(self, response):
        open_in_browser(response)
        test = response.xpath('//h5[@class="m-2"]/text()').get()
        print(test)
