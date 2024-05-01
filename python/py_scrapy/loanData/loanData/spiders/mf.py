import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer

class LinkSpider(scrapy.Spider):
    name = 'mf3'
    start_urls = ['https://www.mahindrafinance.com/']

    def parse(self, response):
        le = LinkExtractor()
        links = le.extract_links(response)
        for link in links:
            yield {
                'url': link.url
            }

@defer.inlineCallbacks
def crawl():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'urls_list.json',
        'LOG_ENABLED': False
    })
    yield process.crawl(LinkSpider)
    reactor.stop()

crawl()
reactor.run()
