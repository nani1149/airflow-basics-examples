from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 28),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'multi_task_dag',
    default_args=default_args,
    description='A multi-task DAG',
    schedule_interval=timedelta(days=1),
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

def print_hello():
    return "Hello, Airflow!"

t2 = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

t3 = BashOperator(
    task_id='list_files',
    bash_command='ls /',
    dag=dag,
)

t1 >> t2 >> t3
