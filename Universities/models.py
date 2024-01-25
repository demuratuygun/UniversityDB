from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

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


class University(Base):
    __tablename__ = 'university'

    code = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    type = Column(Enum('devlet', 'vakif', 'kktc', 'yurtdisi'))
    city = Column(String)

class Program(Base):
    __tablename__ = 'program'

    entryYear = Column(Integer)
    uni_code = Column(Integer, ForeignKey('university.code'))
    code = Column(Integer, primary_key=True)
    name = Column(String)
    faculty = Column(String)
    scoreType = Column(String)
    scholarship = Column(Integer)
    university = relationship('University', backref='programs')
    admissions = relationship('Admissions', back_populates='program')

class HighSchool(Base):
    __tablename__ = 'highschool'

    name = Column(String, primary_key=True)
    type = Column(String)
    city = Column(String)
    district = Column(String)

class Placement(Base):
    __tablename__ = 'placement'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    school = Column(String, ForeignKey('highschool.name'), primary_key=True)
    recentGrad = Column(Integer)
    prevGrad = Column(Integer)

class TheDux(Base):
    __tablename__ = 'thedux'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    school = Column(String, ForeignKey('highschool.name'), primary_key=True)
    byDuxQuota = Column(Boolean)

class Admissions(Base):
    __tablename__ = 'admissions'

    prgCode = Column(Integer, ForeignKey('program.code'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('program.entryYear'), primary_key=True)
    Quota = Column(Integer)
    duxQuota = Column(Integer)
    placed = Column(Integer)
    genderRatio = Column(Float)
    ceilPoint = Column(Float)
    floorPoint = Column(Float)
    duxFloorPoint = Column(Float)
    ceilRank = Column(Integer)
    floorRank = Column(Integer)
    duxFloorRank = Column(Integer)
    apllicantsNumber = Column(Integer)
    avgPreferenceOrder = Column(Float)
    timesPreferredInFirstOrder = Column(Integer)
    timesPreferredInUpTo3 = Column(Integer)
    timesPreferredInUpTo9 = Column(Integer)
    program = relationship('Program', back_populates='admissions')
    last_admittee = relationship('LastAdmittee', back_populates='admissions')

class LastAdmittee(Base):
    __tablename__ = 'lastadmittee'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    HSGraduation = Column(Integer)
    HSFiled = Column(String)
    point = Column(Float)
    rank = Column(Integer)
    coefficient = Column(Float)
    OBPoint = Column(Float)
    grade = Column(Float)
    gender = Column(Enum('erkek', 'kiz'))
    city = Column(String)

class TYT(Base):
    __tablename__ = 'tyt'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    avgOBPoint = Column(Float)
    floorOBPoint = Column(Float)
    avgGrade = Column(Float)
    avgTYTpoint = Column(Float)
    floorTYTpoint = Column(Float)
    avgTYTrank = Column(Integer)
    floorTYTrank = Column(Integer)
    netTurk = Column(Float)
    netMat = Column(Float)
    netSos = Column(Float)
    netFen = Column(Float)

class AvgSAYNet(Base):
    __tablename__ = 'avgsaynet'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    AYTmat = Column(Float)
    AYTkim = Column(Float)
    AYTfiz = Column(Float)
    AYTbio = Column(Float)

class AvgEANet(Base):
    __tablename__ = 'avgeanet'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    AYTmat = Column(Float)
    AYTedeb = Column(Float)
    AYTtarih1 = Column(Float)
    AYTcog1 = Column(Float)

class AvgSOZNet(Base):
    __tablename__ = 'avgsoznet'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    AYTedeb = Column(Float)
    AYTtarih1 = Column(Float)
    AYTcog1 = Column(Float)
    AYTtarih2 = Column(Float)
    AYTcog2 = Column(Float)
    AYTfelsefe = Column(Float)
    AYTdin = Column(Float)

class AvgDILNet(Base):
    __tablename__ = 'avgdilnet'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    AYTdil = Column(Float)

class PreferredUniversities(Base):
    __tablename__ = 'preferreduniversities'

    prgCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    uni_code = Column(Integer, ForeignKey('university.code'), primary_key=True)
    frequency = Column(Integer)

class PreferredPrograms(Base):
    __tablename__ = 'preferredprograms'

    admtCode = Column(Integer, ForeignKey('admissions.prgCode'), primary_key=True)
    entryYear = Column(Integer, ForeignKey('admissions.entryYear'), primary_key=True)
    prgcode = Column(Integer, ForeignKey('program.code'), primary_key=True)
    frequency = Column(Integer)