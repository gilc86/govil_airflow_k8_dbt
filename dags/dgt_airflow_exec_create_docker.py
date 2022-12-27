from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import os

with DAG(
        dag_id="dgt_airflow_exec_create_docker",
        start_date=datetime(2022, 8, 1),
        schedule_interval=None,
        catchup=False
) as dag:
    execute_my_script = BashOperator(
        task_id="dgt_airflow_exec_create_docker",
        # Note the space at the end of the command!
        # bash_command="$AIRFLOW_HOME/include/my_bash_script.sh "
        bash_command="/home/gilc/projects/script_exec/exec_create_docker_dgt_govil_dbt.sh "
        # since the env argument is not specified, this instance of the
        # BashOperator has access to the environment variables of the Airflow
        # instance like AIRFLOW_HOME
    )
