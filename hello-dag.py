from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

def hello_world():
    print("Hello World!")

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

with DAG(
    'hello-world',
    description='A DAG for Saying Hello',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['hello','example'],
) as dag:
    
    say_hello = PythonOperator(
        task_id="hello_world",
        python_callable=hello_world)

    say_hello
