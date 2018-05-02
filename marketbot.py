#Data Mining using Bloomberg and Scrapy

import scrapy


class MarketbotSpider(scrapy.Spider):
    name = 'marketbot'
    allowed_domains = ['https://www.bloomberg.com/quote/SPX:IND','https://www.bloomberg.com/quote/BCOMTR:IND','https://www.bloomberg.com/quote/DXY:CUR','https://www.bloomberg.com/quote/EXI:US']
    start_urls = ['http://https://www.bloomberg.com/quote/SPX:IND/','https://www.bloomberg.com/quote/BCOMTR:IND','https://www.bloomberg.com/quote/DXY:CUR','https://www.bloomberg.com/quote/EXI:US']

    def parse(self, response):
        pass
        Name = response.css(".name::text").extract()
        Price = response.css(".price::text").extract()
        Time = response.css(".price-datetime::text").extract()


        for item in zip(Name,Price,Time):
            #create a dictionary to store the scraped info
            scraped_info = {
                'Name' : item[0],
                'Price' : item[1],
                'Time' : item[2],
            }

            yield scraped_info
