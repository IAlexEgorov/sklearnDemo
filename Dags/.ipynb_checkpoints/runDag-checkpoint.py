import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

path = "/opt/airflow/dags/repo/dags/model.py"

dag = DAG(
        'runDag',
        start_date=days_ago(0,0,0,0,0)
    )

model_run = BashOperator(task_id='model_run', bash_command=f"python3 {path}", dag=dag)


model_run
