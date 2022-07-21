from datetime import datetime, timedelta
from pprint import pprint

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id='hello-world',
    description='A DAG for Saying Hello',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['hello','example'],
) as dag:
    
    @task(task_id="say_hello")
    def hello_world(ds=None, **kwargs):
        pprint(kwargs)
        print(ds)
        print("Hello World!")
        
        return "Howdy"
        
    howdy = hello_world()
