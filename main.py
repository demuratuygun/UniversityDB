from scrapy.crawler import CrawlerProcess
from scrapy import signals

from Universities.spiders.Universities import UniversitySpider
from Universities.spiders.Programs import ProgramSpider

import threading
import json




#scrapy crawl universities -o universities.json
def universitiesSpider():
    
    process = CrawlerProcess(settings={
        "FEEDS": {
            "universities.json": {"format": "json"},
        },
    })

    process.crawl(UniversitySpider)
    process.signals.connect(programsSpider, signal=signals.spider_closed)
    process.start()



#scrapy crawl programs -o programs.json
def programsSpider():
    
    universities = []
    with open('universities.json', 'r') as file:
        universities = json.load(file)

    process = CrawlerProcess(settings={
        "FEEDS": {
            "programs.json": {"format": "json"},
        },
    })

    process.crawl(ProgramSpider, uni_codes=[uni["univCode"] for uni in universities])
    process.start()



universitiesSpider()
#programsSpider()

def threding_example():

    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()