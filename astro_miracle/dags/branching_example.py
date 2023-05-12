from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import datetime

def choose_next_task(**kwargs):
    # Get the value of the previous task
    prev_task_result = kwargs['ti'].xcom_pull(task_ids='previous_task')
    
    # Determine the next task based on the previous task's result
    if prev_task_result == 'success':
        return 'task_a'
    else:
        return 'task_b'

with DAG(dag_id='branching', start_date=datetime(2022, 1, 1), schedule_interval='@daily') as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello from Task 1"',
        dag=dag
    )
    
    previous_task = BashOperator(
        task_id='previous_task',
        bash_command='echo "Not success"',
        dag=dag
    )

    branch_task = BranchPythonOperator(
        task_id='branch_task',
        python_callable=choose_next_task,
        dag=dag
    )

    task_a = BashOperator(
        task_id='task_a',
        bash_command='echo "Hello from Task A"',
        dag=dag
    )

    task_b = BashOperator(
        task_id='task_b',
        bash_command='echo "Hello from Task B"',
        dag=dag
    )

    task_1 >> previous_task >> branch_task >> [task_a, task_b]
