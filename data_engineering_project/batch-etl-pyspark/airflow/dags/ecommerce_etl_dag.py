from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from datetime import datetime
import os

from src.utils.spark_session import create_spark_session
from src.etl.extract import extract_customers, extract_products, extract_orders
from src.etl.transform import transform_data
from src.etl.load import load_data

def run_etl():
    spark = create_spark_session()
    orders = extract_orders(spark)
    customers = extract_customers(spark)
    products = extract_products(spark)
    enriched_df = transform_data(orders, customers, products)
    load_data(enriched_df, os.getenv("OUTPUT_PATH"))

with DAG("ecommerce_etl", start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    etl_task = PythonOperator(task_id="run_etl", python_callable=run_etl)