import scrapy
import json
import os

class MySpider(scrapy.Spider):
    name = 'mf2'
    custom_settings = {
            'FEEDS': {'Loan_data6.json': {'format': 'json'}}
        }
    
    
    def load_json_link():
        try:
            path1 = os.getcwd()
            path2 = "loanData\\loandata\\output6.json"
            
            files1 = os.path.join(path1, path2)
            print(files1)
           
            with open(files1, 'r') as file:
                data = json.load(file)
        except Exception as e:
            print(e)
            return
        return data
    
    
    def start_requests(self):
        
        loan_data = self.load_json_link()

        for loan_info in loan_data:
            loan_type = loan_info.get('Loan Name')
            loan_link = loan_info.get('Loan Link')
            yield scrapy.Request(url=loan_link, callback=self.parse_details, meta={'loan_type': loan_type})

    
    def parse_details(self, response):
        title = response.css('.twoColumnft h2::text').get()
        paragraphs = response.xpath('//div[@class="col col-6 twoColumnft"]/p//text()').extract()
        description = ' '.join(paragraphs).strip()

        yield {
            "Title": title,
            "Description": description,
        }
        self.writeTotxt('Loan_data6.json')


    def writeTotxt(file1):
        data = json.load(open(file1))

        with open('loan_details.txt', 'w') as file:
            for item in data:
                file.write("Title: {}\n".format(item["Title"]))
                file.write("Description: {}\n\n".format(item["Description"]))    

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'LOG_ENABLED': False  
    })
    process.crawl(MySpider)
    process.start()
