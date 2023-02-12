# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader.processors import 
from itemloaders.processors import MapCompose, TakeFirst

class UniversityItem(scrapy.Item):

    univCode = scrapy.Field(output_processor=TakeFirst())
    univName = scrapy.Field(output_processor=TakeFirst())
    univType = scrapy.Field(output_processor=TakeFirst())


class ProgramItem(scrapy.Item):

    university= scrapy.Field(output_processor=TakeFirst())
    program = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    type = scrapy.Field(output_processor=TakeFirst())
    faculty = scrapy.Field(
        input_processor=MapCompose(lambda s: s.strip("()")),
        output_processor=TakeFirst()
    )
    code = scrapy.Field(
        input_processor=MapCompose(lambda s: s.split("y=")[1]),
        output_processor=TakeFirst()
    )


class GeneralInfoItem(scrapy.Item):

    col1 = scrapy.Field()
    col2 = scrapy.Field(
        input_processor=MapCompose(int),
        output_processor=TakeFirst()
    )
    