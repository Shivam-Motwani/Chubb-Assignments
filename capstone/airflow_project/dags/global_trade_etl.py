from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def bronze_ingestion():
    pass  # call Databricks job or notebook

def silver_cleaning():
    pass  # call Databricks job

def gold_kpis():
    pass  # call Databricks job

def forecasting():
    pass  # call Databricks job

def emerging_markets():
    pass  # call Databricks job

with DAG('global_trade_pipeline', start_date=datetime(2026,1,1),
         schedule_interval='@daily', catchup=False, default_args={'retries':1}) as dag:

    t1 = PythonOperator(task_id='captone_bronze', python_callable=bronze_ingestion)
    t2 = PythonOperator(task_id='capstone_silver', python_callable=silver_cleaning)
    t3 = PythonOperator(task_id='capstone_gold', python_callable=gold_kpis)
    t4 = PythonOperator(task_id='capstone_forecasting', python_callable=forecasting)
    t5 = PythonOperator(task_id='capstone_emerging_markets', python_callable=emerging_markets)

    t1 >> t2 >> t3 >> t4 >> t5
