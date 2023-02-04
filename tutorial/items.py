# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class UniversityItem(scrapy.Item):

    univCode = scrapy.Field()
    univName = scrapy.Field()
    univType = scrapy.Field()


class ProgramItem(scrapy.Item):
    
    university= scrapy.Field()
    program = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    type = scrapy.Field()
    faculty = scrapy.Field(
        input_processor=MapCompose(lambda s: s.strip("()")),
        output_processor=TakeFirst()
    )
    code = scrapy.Field(
        input_processor=MapCompose(lambda s: s.split("y=")[1]),
        output_processor=TakeFirst()
    )

