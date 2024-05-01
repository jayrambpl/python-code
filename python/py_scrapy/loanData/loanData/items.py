import scrapy
from scrapy.item import Item, Field

class LoanDataItem(Item):
    title = Field()
    url = Field()
    description = Field()
    pass
