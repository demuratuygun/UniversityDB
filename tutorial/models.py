
from sqlalchemy import create_engine, ForeignKey, Column, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, Date, DateTime, Float, Boolean, Text)

from scrapy.utils.project import get_project_settings


Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"), echo=True)


def create_table(engine):
    Base.metadata.create_all(engine)


class GeneralInfo(Base):
    __tablename__ = "General_Info"

    col_1 = Column('Program', Text())
    col_2 = Column('Sene', Integer, primary_key=True)
    col_3 = Column('ÖSYM Program Kodu', Text(), primary_key=True)
    col_4 = Column('Üniversite Türü', Text())
    col_5 = Column('Üniversite', Text())
    col_6 = Column('Fakülte / Yüksekokul', Text())
    col_7 = Column('Puan Türü', Text())
    col_8 = Column('Burs Türü', Text())

    col_9 = Column('Genel Kontenjan', Integer)
    col_10 = Column('Okul Birincisi Kontenjanı', Integer)
    col_11 = Column('Toplam Kontenjan', Integer)
    col_12 = Column('Genel Kontenjana Yerleşen', Integer)
    col_13 = Column('Okul Birincisi Kontenjanına Yerleşen', Integer)
    col_14 = Column('Toplam Yerleşen', Integer)
    col_15 = Column('Boş Kalan Kontenjan', Integer)
    col_16 = Column('İlk Yerleşme Oranı', Float)
    col_17 = Column('Yerleşip Kayıt Yaptırmayan', Integer)
    col_18 = Column('Ek Yerleşen', Integer)

    col_19 = Column('0,12 Katsayı ile Yerleşen Son Kişinin Puanı*', Float)
    col_20 = Column('0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Puanı*', Float)
    col_21 = Column('0,12 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*', Integer)
    col_22 = Column('0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*', Integer)
    col_23 = Column('2022 Tavan Puan(0,12)*', Float)
    col_24 = Column('2022 Tavan Başarı Sırası(0,12)*', Integer)
    col_25 = Column("2021'de Yerleşip 2022'de OBP'si Kırılarak Yerleşen Sayısı*", Integer)
    col_26 = Column("Yerleşenlerin Ortalama OBP'si*", Float)
    col_27 = Column('Yerleşenlerin Ortalama Diploma Notu*', Float)

