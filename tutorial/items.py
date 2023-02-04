# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class UniversityItem(scrapy.Item):
    # define the fields for your item here like:
    univCode = scrapy.Field()
    univName = scrapy.Field()
    univType = scrapy.Field()


class ProgramLinkItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    university = scrapy.Field()
    program = scrapy.Field()
    score_type = scrapy.Field()
    faculty = scrapy.Field()
    link = scrapy.Field()