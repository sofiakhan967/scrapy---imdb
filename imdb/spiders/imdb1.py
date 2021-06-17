import scrapy
import logging

class Imdb1Spider(scrapy.Spider):
    name = 'imdb1'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
       for movie in response.xpath('//td[@class="titleColumn"]'):
        
               title = movie.xpath('.//a/text()').get()
               link = movie.xpath('.//a/@href').get()
               yield response.follow(url=link,callback=self.movie_parse,meta={'Name':title})



    def movie_parse(self, response):
       # logging.info(response.url)
        title=response.request.meta['Name']
        #print(title)
        for row in response.xpath('//div[@class="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-4 cgfrOx"]'):
            yield{
               'Name':title,
               'year':row.xpath('.//ul/li/span[@class="TitleBlockMetaData__ListItemText-sc-12ein40-2 jedhex"][1]/text()').get(),
               'time':row.xpath('.//ul/li[@class="ipc-inline-list__item"][3]/text()').get(),
               'rating':response.xpath('//div[@class="AggregateRatingButton__Rating-sc-1il8omz-2 ckpPOV"]/span[@class="AggregateRatingButton__RatingScore-sc-1il8omz-1 fhMjqK"]/text()').get(),
               'url':response.url
            }

           
            
        
