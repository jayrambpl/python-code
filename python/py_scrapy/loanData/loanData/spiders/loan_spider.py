import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from loanData.items import LoanDataItem 


class MFSpider(CrawlSpider):
    name = "mf0"
    allowed_domains = ["mahindrafinance.com"]
    start_urls = ["https://www.mahindrafinance.com/"]
    custom_settings = {
        # 'DOWNLOAD_DELAY': 2,
        # 'CONCURRENT_REQUESTS': 2,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
        # 'CONCURRENT_REQUESTS_PER_IP': 2,
        # 'COOKIES_ENABLED': True,
        # 'COOKIES_DEBUG': True,
        # 'DOWNLOAD_TIMEOUT': 10,
        # 'RETRY_ENABLED': True,
        # 'RETRY_TIMES': 3,
        # 'RETRY_HTTP_CODES': [500, 501, 502, 503, 504, 400, 403, 404, 408, 429],
        # 'REDIRECT_ENABLED': True,
        # 'AUTOTHROTTLE_ENABLED': True,
        # 'AUTOTHROTTLE_START_DELAY': 5,
        # 'AUTOTHROTTLE_MAX_DELAY': 60,
        # 'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
        # 'AUTOTHROTTLE_DEBUG': True,
        'FEEDS': {'data.json': {'format': 'json'}}

    }
    rules = (
        Rule(
            LinkExtractor(allow=("/loans/", "/sme-loans/"), deny=("/loans/*/emi-calculator",)),
            callback="parse",
            follow=True
        ),
    )

    def parse(self, response):
        tab_box = response.css('div.tabBox')
        for box in tab_box:
            title = box.css('h3::text').get().strip()
            link = box.css('a.whiteBtn::attr(href)').get()
           
            if title and link:
                Loan_Data_Items = LoanDataItem()
                Loan_Data_Items['title'] = title
                Loan_Data_Items['url'] = link
                yield Loan_Data_Items

    #     print(f"Requesting: {link}")
    #     yield scrapy.Request(url=link, callback=self.parse_details, meta={'title': title})

    #     # Print the extracted links for debugging
    #     extracted_links = [link.url for link in self.rules[0].link_extractor.extract_links(response)]
    #     print(f"Extracted Links: {extracted_links}")

    # def parse_details(self, response):
    #     title = response.meta.get('title')
    #     print(f"Response status code: {response.status}")
    #     print(f"Parsing details for: {title}")

    #     paragraphs = response.css('div.twoColumnft p::text').getall()

    #     print(f"Title: {title}")
    #     print(f"Paragraphs: {paragraphs}")

    #     yield {
    #         title: ' '.join(paragraphs).strip(),
    #     }
