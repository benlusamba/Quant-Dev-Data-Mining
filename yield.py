import scrapy


class YieldSpider(scrapy.Spider):
    name = 'yield'
    allowed_domains = ['https://www.bloomberg.com/quote/FDFD:IND','https://www.bloomberg.com/quote/PRIME:IND','https://www.bloomberg.com/quote/FDTR:IND']
    start_urls = ['https://www.bloomberg.com/quote/FDFD:IND','https://www.bloomberg.com/quote/PRIME:IND','https://www.bloomberg.com/quote/FDTR:IND']

    def parse(self, response):
        pass
        Name = response.css(".name::text").extract()
        Rate = response.css(".price::text").extract()
        Time = response.css(".price-datetime::text").extract()


        for item in zip(Name,Rate,Time):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Name' : item[0],
                'Rate' : item[1],
                'Time' : item[2],
            }

            yield scraped_info
