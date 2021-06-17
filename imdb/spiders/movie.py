import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']
#link of the object u wantg to scrape 
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
       # response.url
        yield{
            'title':response.xpath('//div[@class="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt"]/h1/text()').get(),
            'year':response.xpath('//span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"]/text()').get(),
            'duration':response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-4 cgfrOx"]/ul/li[@class="ipc-inline-list__item"][3]/text()').get(),
            'genre':response.xpath('//span[@class="ipc-chip__text"][1]/text()').get()
             }
