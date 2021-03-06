import scrapy


class MetalSpider(scrapy.Spider):
    name = 'metal'
    allowed_domains = ['https://www.bloomberg.com/quote/GC1:COM','https://www.bloomberg.com/quote/HG1:COM']
    start_urls = ['https://www.bloomberg.com/quote/GC1:COM','https://www.bloomberg.com/quote/HG1:COM']

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
