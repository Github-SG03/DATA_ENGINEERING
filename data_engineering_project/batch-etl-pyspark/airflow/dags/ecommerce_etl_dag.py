from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime

def dummy_task():
    print("ETL running!")

with DAG(
    dag_id="ecommerce_etl_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=dummy_task,
    )