from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG('hour_dag', default_args=default_args, schedule_interval=timedelta(hours=1)) as dag1:
    t1 = BashOperator(task_id='task_1', bash_command='echo "Hello from Task 1"')

with DAG('30mins_dag', default_args=default_args, schedule_interval='*/30 * * * *') as dag2:
    t2 = BashOperator(task_id='task_2', bash_command='echo "Hello from Task 2"')

with DAG('not_scheduled_dag', default_args=default_args, schedule_interval=None) as dag3:
    t3 = BashOperator(task_id='task_3', bash_command='echo "Hello from Task 3"')

with DAG('midnight_dag', default_args=default_args, schedule_interval='0 0 * * *') as dag4:
    t4 = BashOperator(task_id='task_4', bash_command='echo "Hello from Task 4"')
