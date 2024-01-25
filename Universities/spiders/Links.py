import scrapy
import json
import os

from scrapy.loader import ItemLoader
from Universities.items import ProgramItem



#scrapy crawl programs -o programs.json
class LinksSpider(scrapy.Spider):

    name = "links"
    def __init__(self, uni_codes):
        os.remove("programs.json")
        self.start_urls = ["https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y=106510077"]
 
    
    def parse(self, response):
        
        
        print(response)
        
