import scrapy
import json
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class MFSpider(scrapy.Spider):
    name = 'mf'
    allowed_domains = ["mahindrafinance.com"]
    start_urls = ['https://www.mahindrafinance.com/sme-loans', 'https://www.mahindrafinance.com/loans']
    custom_settings = {
        'FEEDS': {'Loan_data7.json': {'format': 'json'}}
    }

    rules = (
        Rule(
            LinkExtractor(allow=('/sme-loans/.+', ), deny=('/emi-calculator',)),
            callback='parse_sme_loan',
            follow=True
        ),
        Rule(
            LinkExtractor(allow=('/loans/.+',)),
            callback='parse_loan',
            follow=True
        ),
    )
    
    def __init__(self, *args, **kwargs):
        super(MFSpider, self).__init__(*args, **kwargs)
        self.visited_links = set()

    def parse_link(self, response):
        links = response.css('a::attr(href)').extract()
        for link in links:
            if link.startswith('/loans/') or link.startswith('/sme-loans/'):
                full_url = response.urljoin(link)
                if full_url not in self.visited_links:
                    self.visited_links.add(full_url)

    def closed(self, reason):
        if self.visited_links:
            with open('Loan_data7.json', 'w') as f:
                json.dump(list(self.visited_links), f)
        else:
            print("No links found to save.")

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'LOG_ENABLED': False
    })
    process.crawl(MFSpider)
    process.start()
