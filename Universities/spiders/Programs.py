import scrapy
import json
import os

from scrapy.loader import ItemLoader
from Universities.items import ProgramItem

#scrapy crawl programs -o programs.json
class ProgramSpider(scrapy.Spider):

    name = "programs"
    def __init__(self, uni_codes):
        os.remove("programs.json")
        self.start_urls = ["https://yokatlas.yok.gov.tr/lisans-univ.php?u="+code for code in uni_codes[0:2]]
 
    
    def parse(self, response):

        for button in response.xpath("//a[contains(@href, 'lisans.php?y=')]"):

            loader = ItemLoader(item=ProgramItem(), selector=button)
            loader.add_xpath("university", "//h3/text()")
            loader.add_xpath("program", "div/text()")
            loader.add_xpath("type", "button/text()")
            loader.add_xpath("faculty", "small/font/text()")
            loader.add_xpath("code", "@href")

            yield loader.load_item()

