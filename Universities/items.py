# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader.processors import 
from itemloaders.processors import MapCompose, TakeFirst


class UniversityItem(scrapy.Item):
    code  = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    type = scrapy.Field(output_processor=TakeFirst())
    city = scrapy.Field(output_processor=TakeFirst())

class ProgramItem(scrapy.Item):
    code = scrapy.Field(
        input_processor=MapCompose(lambda s: s.split("y=")[1]),
        output_processor=TakeFirst()
    )
    entryYear = scrapy.Field(output_processor=TakeFirst())
    uniCode = scrapy.Field(output_processor=TakeFirst())
    faculty = scrapy.Field(
        input_processor=MapCompose(lambda s: s.strip(" ()")),
        output_processor=TakeFirst()
    )
    name = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    scoreType  = scrapy.Field(output_processor=TakeFirst())
    scholarship  = scrapy.Field(output_processor=TakeFirst())

class HighSchoolItem(scrapy.Item):
    __tablename__ = 'school'
    name  = scrapy.Field(output_processor=TakeFirst())
    type  = scrapy.Field(output_processor=TakeFirst())
    city  = scrapy.Field(output_processor=TakeFirst())
    district  = scrapy.Field(output_processor=TakeFirst())

class PlacementItem(scrapy.Item):
    __tablename__ = 'Placement'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    school  = scrapy.Field(output_processor=TakeFirst())
    recentGrad  = scrapy.Field(output_processor=TakeFirst())
    prevGrad  = scrapy.Field(output_processor=TakeFirst())

class TheDuxItem(scrapy.Item):
    __tablename__ = 'theDux'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    school  = scrapy.Field(output_processor=TakeFirst())
    byDuxQuota  = scrapy.Field(output_processor=TakeFirst())

class AdmissionsItem(scrapy.Item):
    __tablename__ = 'admt'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    Quota  = scrapy.Field(output_processor=TakeFirst())
    duxQuota  = scrapy.Field(output_processor=TakeFirst())
    placed  = scrapy.Field(output_processor=TakeFirst())
    genderRatio  = scrapy.Field(output_processor=TakeFirst())
    ceilPoint  = scrapy.Field(output_processor=TakeFirst())
    floorPoint  = scrapy.Field(output_processor=TakeFirst())
    duxFloorPoint  = scrapy.Field(output_processor=TakeFirst())
    ceilRank  = scrapy.Field(output_processor=TakeFirst())
    floorRank  = scrapy.Field(output_processor=TakeFirst())
    duxFloorRank  = scrapy.Field(output_processor=TakeFirst())
    apllicantsNumber  = scrapy.Field(output_processor=TakeFirst())
    avgPreferenceOrder  = scrapy.Field(output_processor=TakeFirst())
    timesPreferredInFirstOrder  = scrapy.Field(output_processor=TakeFirst())
    timesPreferredInUpTo3  = scrapy.Field(output_processor=TakeFirst())
    timesPreferredInUpTo9  = scrapy.Field(output_processor=TakeFirst())

class LastAdmitteeItem(scrapy.Item):
    __tablename__ = 'lastAdmittee'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    HSGraduation  = scrapy.Field(output_processor=TakeFirst())
    HSFiled  = scrapy.Field(output_processor=TakeFirst())
    point  = scrapy.Field(output_processor=TakeFirst())
    rank  = scrapy.Field(output_processor=TakeFirst())
    coefficient  = scrapy.Field(output_processor=TakeFirst())
    OBPoint  = scrapy.Field(output_processor=TakeFirst())
    grade  = scrapy.Field(output_processor=TakeFirst())
    gender  = scrapy.Field(output_processor=TakeFirst())
    city  = scrapy.Field(output_processor=TakeFirst())

class TYTItem(scrapy.Item):
    __tablename__ = 'TYT'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    avgOBPoint  = scrapy.Field(output_processor=TakeFirst())
    floorOBPoint  = scrapy.Field(output_processor=TakeFirst())
    avgGrade  = scrapy.Field(output_processor=TakeFirst())
    avgTYTpoint  = scrapy.Field(output_processor=TakeFirst())
    floorTYTpoint  = scrapy.Field(output_processor=TakeFirst())
    avgTYTrank  = scrapy.Field(output_processor=TakeFirst())
    floorTYTrank  = scrapy.Field(output_processor=TakeFirst())
    netTurk  = scrapy.Field(output_processor=TakeFirst())
    netMat  = scrapy.Field(output_processor=TakeFirst())
    netSos  = scrapy.Field(output_processor=TakeFirst())
    netFen  = scrapy.Field(output_processor=TakeFirst())

class AvgSAYNetItem(scrapy.Item):
    __tablename__ = 'avgSAYNet'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    AYTmat  = scrapy.Field(output_processor=TakeFirst())
    AYTkim  = scrapy.Field(output_processor=TakeFirst())
    AYTfiz  = scrapy.Field(output_processor=TakeFirst())
    AYTbio  = scrapy.Field(output_processor=TakeFirst())

class AvgEANetItem(scrapy.Item):
    __tablename__ = 'avgEANet'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    AYTmat  = scrapy.Field(output_processor=TakeFirst())
    AYTedeb  = scrapy.Field(output_processor=TakeFirst())
    AYTtarih1  = scrapy.Field(output_processor=TakeFirst())
    AYTcog1  = scrapy.Field(output_processor=TakeFirst())

class AvgSOZNetItem(scrapy.Item):
    __tablename__ = 'avgSOZNet'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    AYTedeb  = scrapy.Field(output_processor=TakeFirst())
    AYTtarih1  = scrapy.Field(output_processor=TakeFirst())
    AYTcog1  = scrapy.Field(output_processor=TakeFirst())
    AYTtarih2  = scrapy.Field(output_processor=TakeFirst())
    AYTcog2  = scrapy.Field(output_processor=TakeFirst())
    AYTfelsefe  = scrapy.Field(output_processor=TakeFirst())
    AYTdin  = scrapy.Field(output_processor=TakeFirst())

class AvgDILNetItem(scrapy.Item):
    __tablename__ = 'avgDILNet'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    AYTdil  = scrapy.Field(output_processor=TakeFirst())

class PreferredUniversitiesItem(scrapy.Item):
    __tablename__ = 'pu'
    prgCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    uni_code  = scrapy.Field(output_processor=TakeFirst())
    frequency  = scrapy.Field(output_processor=TakeFirst())

class PreferredProgramsItem(scrapy.Item):
    __tablename__ = 'pp'
    admtCode  = scrapy.Field(output_processor=TakeFirst())
    entryYear  = scrapy.Field(output_processor=TakeFirst())
    prgcode  = scrapy.Field(output_processor=TakeFirst())
    frequency  = scrapy.Field(output_processor=TakeFirst())
