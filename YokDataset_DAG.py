from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

import json
import sys
sys.path.append('/home/maverick/data-science/universities/tutorial')

from scrapy.crawler import CrawlerProcess
from tutorial.spiders.Universities import UniversitySpider
from tutorial.spiders.Programs import ProgramSpider


default_dag_args = {
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1324
}


#scrapy crawl universities -o universities.json
def universitiesSpider():
    
    process = CrawlerProcess(settings={
        "FEEDS": {
            "/home/maverick/data-science/universities/tutorial/universities.json": {"format": "json"},
        },
    })

    process.crawl(UniversitySpider)
    process.start()

    
    with open('/home/maverick/data-science/universities/tutorial/universities.json', 'r') as file:
        universities = json.load(file)




#scrapy crawl programs -o programs.json
def programsSpider():

    universities = []
    with open('/home/maverick/data-science/universities/tutorial/universities.json', 'r') as file:
        universities = json.load(file)


    process = CrawlerProcess(settings={
        "FEEDS": {
            "/home/maverick/data-science/universities/tutorial/programs.json": {"format": "json"},
        },
    })

    process.crawl(ProgramSpider, uni_codes=[uni["univCode"] for uni in universities])
    process.start()


# definign our dag
with DAG("YokDataset_DAG", schedule_interval = None, default_args = default_dag_args) as dag:
    
    # defining the task of the DAG
    task_0 = BashOperator(
        task_id='bash_task', 
        bash_command=""
    )
    task_1 = PythonOperator(
        task_id='universities_spider',
        python_callable=universitiesSpider
    )
    task_2 = PythonOperator(
        task_id='programs_spider',
        python_callable=programsSpider,
        #op_kwargs={'random_base': 3},
    )

    # dependencies between tasks >> <<
    task_0 >> task_1 >> task_2