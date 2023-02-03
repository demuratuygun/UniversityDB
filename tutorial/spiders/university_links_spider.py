import scrapy
import json

from scrapy.loader import ItemLoader
from tutorial.items import UniversityItem

#scrapy crawl university_codes -o university_codes.json
class UniversityLinksSpider(scrapy.Spider):
    name = "university_codes"
    start_urls = ["https://yokatlas.yok.gov.tr/lisans-anasayfa.php"]

    def parse(self, response):

        groups = response.xpath("//select[@id='univ']/optgroup")

        for group in groups:

            uniType = group.attrib['label']
            for option in group.xpath("option"):

                loader = ItemLoader(item=UniversityItem(), selector=option)
                loader.add_xpath("code", "@value")
                loader.add_xpath("name", "text()")
                loader.add_value("utype", uniType)
                yield loader.load_item()



#scrapy crawl program_links -o program_links.json
class ProgramLinksSpider(scrapy.Spider):
    name = "program_links"

    uniCodes = []
    with open('university_codes.json', 'r') as file:
        uniCodes = json.load(file)

    start_urls = ["https://yokatlas.yok.gov.tr/lisans-univ.php?u="+uni["code"] for uni in uniCodes]
 
    def parse(self, response):

        for button in response.xpath("//a[contains(@href, 'lisans.php?y=')]"):
            yield {
                "university": response.xpath("//h3/text()").get(),
                "program": button[0].xpath("div/text()").get().strip(),
                "score type": button.xpath("button/text()").get(),
                "faculty": button.xpath("small/font/text()").get().strip("()"),
                "link": button.attrib["href"]
            }



class IpTest(scrapy.Spider):
    name = "IpTest"
    start_urls = ["https://sveltekit-on-the-edge.vercel.app/"]

    def parse(self, response):
        
        print(response.url)
        data = response.xpath("//strong/text()")
        print(data[0], data[1])

