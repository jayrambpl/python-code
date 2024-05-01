import scrapy
import json
import os

class MySpider(scrapy.Spider):
    name = 'mf3'
    custom_settings = {
            'FEEDS': {'Loan_data.json': {'format': 'json'}}
        }
        
    def load_json_link(self):
        try:
            path1 = os.getcwd()
            path2 = "all_url.json"
            
            files1 = os.path.join(path1, path2)
            print(files1)
           
            with open(files1, 'r') as file:
                data = json.load(file)
        except Exception as e:
            print(e)
            return
        return data
    

    def get_url(self):
        unique_urls = set()
        try:
            loan_data = self.load_json_link()
        except Exception as e:
            print(e)
            return  
        
        for item in loan_data:
            url = item.get("url")
            if 'loans' in url or 'sme-loans' in url:
                unique_urls.add(url)

        unique_urls_list = list(unique_urls)
        return unique_urls_list
    
    def start_requests(self):
        loan_data = self.get_url()
        print(loan_data)
        for loan_url in loan_data:
            yield scrapy.Request(url=loan_url, callback=self.parse_details)

    
    def parse_details(self, response):
        title = response.css('.twoColumnft h2::text').get()
        paragraphs = response.xpath('//div[@class="col col-6 twoColumnft"]/p//text()').extract()
        description = ' '.join(paragraphs).strip()

        yield {
            "Title": title,
            "Description": description,
        }
        # self.writeTotxt('Loan_data6.json')


    # def writeTotxt(file1):
    #     data = json.load(open(file1))

    #     with open('loan_details.txt', 'w') as file:
    #         for item in data:
    #             file.write("Title: {}\n".format(item["Title"]))
    #             file.write("Description: {}\n\n".format(item["Description"]))    

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'LOG_ENABLED': False  
    })
    process.crawl(MySpider)
    process.start()
