from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(dag_id='one_failed_trigger_dag', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Running Task 1"',
        trigger_rule='one_failed'
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='exit 1',
        trigger_rule='one_failed'
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Running Task 3"',
        trigger_rule='one_failed'
    )

    task_4 = BashOperator(
        task_id='task_4',
        bash_command='echo "Running Task 4"',
        trigger_rule='one_failed'
    )

    task_5 = BashOperator(
        task_id='task_5',
        bash_command='echo "Running Task 5"',
        trigger_rule='one_failed'
    )

    task_1 >> [task_2, task_3] >> task_4 >> task_5
