# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from models import *

class TutorialPipeline:
    def process_item(self, item, spider):
        return item


class GeneralInfoPipeline:

    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        
        session = self.Session()
        GInfo = GeneralInfo()

        GInfo.col_1 = item['Program']
        GInfo.col_2 = item['Sene']
        GInfo.col_3 = item['ÖSYM Program Kodu']
        GInfo.col_4 = item['Üniversite Türü']
        GInfo.col_5 = item['Üniversite']
        GInfo.col_6 = item['Fakülte / Yüksekokul']
        GInfo.col_7 = item['Puan Türü']
        GInfo.col_8 = item['Burs Türü']

        GInfo.col_9 = item['Genel Kontenjan']
        GInfo.col_10 = item['Okul Birincisi Kontenjanı']
        GInfo.col_11 = item['Toplam Kontenjan']
        GInfo.col_12 = item['Genel Kontenjana Yerleşen']
        GInfo.col_13 = item['Okul Birincisi Kontenjanına Yerleşen']
        GInfo.col_14 = item['Toplam Yerleşen']
        GInfo.col_15 = item['Boş Kalan Kontenjan']
        GInfo.col_16 = item['İlk Yerleşme Oranı']
        GInfo.col_17 = item['Yerleşip Kayıt Yaptırmayan']
        GInfo.col_18 = item['Ek Yerleşen']

        GInfo.col_19 = item['0,12 Katsayı ile Yerleşen Son Kişinin Puanı*']
        GInfo.col_20 = item['0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Puanı*']
        GInfo.col_21 = item['0,12 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*']
        GInfo.col_22 = item['0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*']
        GInfo.col_23 = item['2022 Tavan Puan(0,12)*']
        GInfo.col_24 = item['2022 Tavan Başarı Sırası(0,12)*']
        GInfo.col_25 = item["2021'de Yerleşip 2022'de OBP'si Kırılarak Yerleşen Sayısı*"]
        GInfo.col_26 = item["Yerleşenlerin Ortalama OBP'si*"]
        GInfo.col_27 = item['Yerleşenlerin Ortalama Diploma Notu*']


        try:
            session.add(GInfo)
            session.commit()

        except:
            session.rollback()
            raise
        
        finally:
            session.close()

        return item;