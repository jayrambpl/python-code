import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LoanSpider(CrawlSpider):
    name = 'mf1'
    allowed_domains = ['mahindrafinance.com']
    start_urls = ['https://www.mahindrafinance.com/sme-loans', 'https://www.mahindrafinance.com/loans']

    rules = (
        Rule(
            LinkExtractor(allow=('/sme-loans', '/loans'), deny=('/emi-calculator',)),
            callback='parse_loan_page',
            follow=True
        ),
        Rule(
            LinkExtractor(allow=('/loans/.+',)),
            callback='parse_loan_details',
            follow=True
        ),
    )

    def parse_loan_page(self, response):
        for tab_box in response.css('div.tabBox'):
            loan_name = tab_box.css('h3::text').get()
            loan_link = tab_box.css('a.whiteBtn::attr(href)').get()
            yield {
                'Loan Name': loan_name,
                'Loan Link': loan_link
            }

    def parse_loan_details(self, response):
        title = response.css('div#overview.twoColumn.product-block div.container div.row.align-center div.col.col-6.twoColumnft h2::text').get()
        description = ' '.join(response.css('div#overview.twoColumn.product-block div.container div.row.align-center div.col.col-6.twoColumnft p::text').getall())
        all_text = ' '.join(response.css('div#overview.twoColumn.product-block div.container::text').getall())
        
        yield {
            'Title': title.strip() if title else None,
            'Description': description.strip() if description else None,
            'All Text': all_text.strip() if all_text else None
        }
