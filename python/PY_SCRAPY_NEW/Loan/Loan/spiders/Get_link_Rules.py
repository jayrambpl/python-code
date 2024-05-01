import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule
from twisted.internet import reactor, defer

class LinkSpider(scrapy.Spider):
    name = 'mf2'
    start_urls = ['https://www.mahindrafinance.com/']

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'url_loan_only.json',
        'LOG_ENABLED': False
    }

    rules = (
        Rule(
            LinkExtractor(allow=(r".*\/(?:loans|sme-loans)\/.*")),
            callback='parse_url',
            follow=True
        ),
    )

    def parse_url(self, response):
        links = LinkExtractor(allow=(r".*\/(?:loans|sme-loans)\/.*")).extract_links(response)
        yield {
            'url': response.url
        }
        print(links)

    # def parse_url(self, response):
    #     yield {
    #         'url': response.url
    #     }

@defer.inlineCallbacks
def crawl():
    process = CrawlerProcess()
    yield process.crawl(LinkSpider)
    reactor.stop()

crawl()
reactor.run()
