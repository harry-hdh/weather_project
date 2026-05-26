import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request')

def main_callable():
    from insert_data import main
    return main()

default_args = {
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2026,5,26),
    'catchup':False
}

dag = DAG(
    dag_id='weather-api-orch',
    default_args=default_args,
    schedule=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='insert_data_task',
        python_callable=main_callable
    )
    #task2