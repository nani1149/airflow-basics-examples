from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_data():
    # Code to extract data from a source
    data = "sample data"
    return data

def process_data(**context):
    # Retrieve data from XCom
    data = context['task_instance'].xcom_pull(task_ids='extract_data')
    # Code to process data
    processed_data = data.upper()
    # Pass data to XCom
    context['ti'].xcom_push(key='processed_data', value=processed_data)

def print_data(**context):
    # Retrieve data from XCom
    data = context['task_instance'].xcom_pull(task_ids='process_data', key='processed_data')
    # Print data
    print(data)

dag = DAG(
    dag_id='xcom_example',
    start_date=datetime(2023, 5, 10),
    schedule_interval=None
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

process_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    provide_context=True,
    dag=dag
)

print_task = PythonOperator(
    task_id='print_data',
    python_callable=print_data,
    provide_context=True,
    dag=dag
)

extract_task >> process_task >> print_task
