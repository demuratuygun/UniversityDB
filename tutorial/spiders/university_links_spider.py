import scrapy
import json

from scrapy.loader import ItemLoader
from tutorial.items import UniversityItem
from tutorial.items import ProgramItem

#scrapy crawl universities -o universities.json
class UniversitySpider(scrapy.Spider):
    name = "universities"
    start_urls = ["https://yokatlas.yok.gov.tr/lisans-anasayfa.php"]

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



#scrapy crawl programs -o program_links.json
class ProgramSpider(scrapy.Spider):
    name = "programs"

    universities = []
    with open('universities.json', 'r') as file:
        universities = json.load(file)

    start_urls = ["https://yokatlas.yok.gov.tr/lisans-univ.php?u="+uni["univCode"] for uni in universities]
 
    def parse(self, response):

        for button in response.xpath("//a[contains(@href, 'lisans.php?y=')]"):

            loader = ItemLoader(item=ProgramItem(), selector=button)
            loader.add_xpath("university", "//h3/text()")
            loader.add_xpath("program", "div/text()")
            loader.add_xpath("type", "button/text()")
            loader.add_xpath("faculty", "small/font/text()")
            loader.add_xpath("code", "@href")
            yield loader.load_item()

            # yield {
            #     "university": response.xpath("//h3/text()").get(),
            #     "program": button[0].xpath("div/text()").get().strip(),
            #     "type": button.xpath("button/text()").get(),
            #     "faculty": button.xpath("small/font/text()").get().strip("()"),
            #     "code": button.attrib["href"].split("y=")[1]
            # }


# https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y=409610488
class TablesSpider(scrapy.Spider):
    name = "tables"

    linksDict = {}
    with open('links.json', 'r') as file:
        linksDict = json.load(file)
    


class IpTest(scrapy.Spider):
    name = "IpTest"
    start_urls = ["https://sveltekit-on-the-edge.vercel.app/"]

    def parse(self, response):
        
        print(response.url)
        data = response.xpath("//strong/text()")
        print(data[0], data[1])

