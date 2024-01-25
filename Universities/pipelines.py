# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from models import *
from items import *

class FilePipeline:
    def process_item(self, item, spider):
        return item


class GeneralInfoPipeline:

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    
    def process_admissions(self, item):
        
        AdmissionsObj = Admissions()

        AdmissionsObj.prgCode = item['prgCode']
        AdmissionsObj.entryYear = item['entryYear']
        AdmissionsObj.Quota = item['Quota']
        AdmissionsObj.duxQuota = item['duxQuota']
        AdmissionsObj.placed = item['placed']
        AdmissionsObj.genderRatio = item['genderRatio']
        AdmissionsObj.ceilPoint = item['ceilPoint']
        AdmissionsObj.floorPoint = item['floorPoint']
        AdmissionsObj.duxFloorPoint = item['duxFloorPoint']
        AdmissionsObj.ceilRank = item['ceilRank']
        AdmissionsObj.floorRank = item['floorRank']
        AdmissionsObj.duxFloorRank = item['duxFloorRank']
        AdmissionsObj.apllicantsNumber = item['apllicantsNumber']
        AdmissionsObj.avgPreferenceOrder = item['avgPreferenceOrder']
        AdmissionsObj.timesPreferredInFirstOrder = item['timesPreferredInFirstOrder']
        AdmissionsObj.timesPreferredInUpTo3 = item['timesPreferredInUpTo3']
        AdmissionsObj.timesPreferredInUpTo9 = item['timesPreferredInUpTo9']

        return AdmissionsObj
    

    def process_university(self, item):

        UniversityObj = University()

        UniversityObj.code = item['code']
        UniversityObj.name = item['name']
        UniversityObj.type = item['type']
        #UniversityObj.city = item['city']

        return UniversityObj
    
    
    def commitRow(session, row):
    
        try:
            session.add(row)
            session.commit()

        except:
            session.rollback()
            raise
        
        finally:
            session.close()


    def process_item(self, item, spider):
        
        session = self.Session()
        
        if isinstance(item, UniversityItem):
            self.process_university(self, item)

        elif isinstance(item, ProgramItem):
            self.process_admissions(self, item)

        self.commitRow(session, item)
        
        return item



