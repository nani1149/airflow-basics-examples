from airflow import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(dag_id='task_group_example', start_date=datetime(2022, 1, 1), schedule_interval='@daily') as dag:
    with TaskGroup('group_1') as group_1:
        task_1 = BashOperator(
            task_id='task_1',
            bash_command='echo "Hello from Task 1"',
            dag=dag
        )

        task_2 = BashOperator(
            task_id='task_2',
            bash_command='echo "Hello from Task 2"',
            dag=dag
        )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "Hello from Task 3"',
        dag=dag
    )

    task_1>>task_2 >> task_3
