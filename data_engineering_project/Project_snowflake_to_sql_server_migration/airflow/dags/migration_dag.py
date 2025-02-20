from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def extract_data():
    # Call the Python script for data extraction from SQL Server
    subprocess.run(['python', 'extract_data.py'])

def load_data():
    # Call the Python script for data loading to Snowflake
    subprocess.run(['python', 'load_data.py'])

def run_dbt_transform():
    # Run dbt transformations using subprocess
    subprocess.run(['dbt', 'run'])

# Define the DAG
dag = DAG('sql_server_to_snowflake_migration',
          description='SQL Server to Snowflake ETL',
          schedule_interval='@daily',  # Schedule as per requirement
          start_date=datetime(2025, 2, 18), catchup=False)

# Task 1: Data Extraction
task_extract = PythonOperator(task_id='extract_data', python_callable=extract_data, dag=dag)

# Task 2: Data Loading to Snowflake
task_load = PythonOperator(task_id='load_data', python_callable=load_data, dag=dag)

# Task 3: dbt Transformation
task_transform = PythonOperator(task_id='dbt_transform', python_callable=run_dbt_transform, dag=dag)

# Set task dependencies
task_extract >> task_load >> task_transform
