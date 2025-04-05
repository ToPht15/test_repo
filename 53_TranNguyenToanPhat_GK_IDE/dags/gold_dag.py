from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json
import os

from app.crawl import crawl_web
from app.transform import transform_data
from app.save import save_price

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 1, 1),
}

def crawl_task_function():
    data = crawl_web()
    return data  

def transform_task_function(**context):
    task_instance = context['task_instance']
    crawled_data = task_instance.xcom_pull(task_ids='crawl_gold')
    
    transformed_data = transform_data(crawled_data)
    return transformed_data  

def save_task_function(**context):
    task_instance = context['task_instance']
    transformed_data = task_instance.xcom_pull(task_ids='transform_gold')
    
    save_price(transformed_data)

with DAG(
    'gold_price_24h',
    default_args=default_args,
    description='Crawl gold prices from 24h.com.vn',
    schedule_interval='0 9 * * *',  
    catchup=False
) as dag:

    crawl_task = PythonOperator(
        task_id='crawl_gold',
        python_callable=crawl_task_function,
    )

    transform_task = PythonOperator(
        task_id='transform_gold',
        python_callable=transform_task_function,
        provide_context=True, 
    )

    save_task = PythonOperator(
        task_id='save_gold',
        python_callable=save_task_function,
        provide_context=True,
    )

    crawl_task >> transform_task >> save_task 