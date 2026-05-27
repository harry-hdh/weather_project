import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api-request')

def main_callable():
    from insert_data import main
    return main()

default_args = {
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2026,5,27),
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
    
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source = '/home/hdh/weather_project/src/weather_project/dbt/my_project',
                 target='/usr/app',
                 type='bind'),
            Mount(source = '/home/hdh/weather_project/src/weather_project/dbt/profiles.yml',
                 target='/root/.dbt/profiles.yml',
                 type='bind')
        ],
        network_mode='weather_project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2