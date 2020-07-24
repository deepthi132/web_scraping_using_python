
import scrapy
from ..items import QuotetItem

class Quotespy(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        items = QuotetItem()
        all_div = response.css('div.quote')
        for div in all_div :
            title = div.css('span.text::text').extract()
            author = div.css('.author::text').extract()
            tag = div.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

#scrapy crawl quotes -o out.csv