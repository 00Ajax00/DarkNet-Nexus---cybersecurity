# crawler/spider.py
import scrapy

class DarkWebSpider(scrapy.Spider):
    name = "darkweb"
    start_urls = ["http://somehiddenservice.onion"]

    def parse(self, response):
        yield {"title": response.css("title::text").get(), "body": response.body[:500]}
