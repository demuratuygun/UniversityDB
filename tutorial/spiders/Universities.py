import scrapy
import json
import os

from scrapy.loader import ItemLoader
from tutorial.items import UniversityItem

#scrapy crawl universities -o universities.json
class UniversitySpider(scrapy.Spider):

    name = "universities"
    start_urls = ["https://yokatlas.yok.gov.tr/lisans-anasayfa.php"]

    def __init__(self):
        os.remove("universities.json")

    def parse(self, response):

        groups = response.xpath("//select[@id='univ']/optgroup")

        for group in groups:

            uniType = group.attrib['label']
            for option in group.xpath("option"):

                loader = ItemLoader(item=UniversityItem(), selector=option)
                loader.add_xpath("univCode", "@value")
                loader.add_xpath("univName", "text()")
                loader.add_value("univType", uniType)
                yield loader.load_item()



# # https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y=409610488
# class TablesSpider(scrapy.Spider):
#     name = "tables"

#     linksDict = {}
#     with open('/home/maverick/data-science/universities/tutorial/links.json', 'r') as file:
#         linksDict = json.load(file)


class IpTest(scrapy.Spider):
    name = "IpTest"
    start_urls = ["https://sveltekit-on-the-edge.vercel.app/"]

    def parse(self, response):
        
        print(response.url)
        data = response.xpath("//strong/text()")
        print(data[0], data[1])

#with open('xd.txt', 'a') as file: file.write(":d\n")