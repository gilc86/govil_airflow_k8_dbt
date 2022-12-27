from datetime import datetime, timedelta
import json
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

gcs_json_path = "/home/airflow/gcs/dags/config_dgt_airflow_k8_dbt.json"
with open(gcs_json_path) as config_file:
    dataConfig = json.load(config_file)
DGT_AIRFLOW_DBT_TAG = dataConfig['Tag_Version']
# DGT_AIRFLOW_DBT_TAG = '1.0.0'

with DAG(
        'dgt_govil_dbt',
        # These args will get passed on to each operator
        # You can override them on a per-task basis during operator initialization
        default_args={
            'depends_on_past': False,
            'email': ['gilc86@gmail.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=60)
        },
        description='A simple tutorial DAG',
        schedule_interval=timedelta(days=1),
        start_date=datetime(2022, 1, 1),
        catchup=False,
        tags=['1.0.0']
) as dag:
    dbt_run = KubernetesPodOperator(
        namespace="k8-executor",  # the new namespace you've created in the Workload Identity creation process
        service_account_name="composer1", # the new k8 service account you've created in the Workload Identity creation process
        image="eu.gcr.io/dgt-gcp-egov-test-govilbi-0/dgt_govil_dbt:"+DGT_AIRFLOW_DBT_TAG,
        # image="eu.gcr.io/dgt-gcp-egov-test-govilbi-0/dgt_govil_dbt@sha256:1ab9f936fcf3c90c7304449278ecb1a8146095c6cce54015bb462d89bc579b96",
        # startup_timeout_seconds=500,
        cmds=["bash", "-cx"],
        # arguments=["cd" , "./dbt/dgt_govil_dbt" , "&& dbt run"], #Liad & Oded
        arguments=["cd /home/dbtuser/dgt_govil_dbt && dbt run"], #Leedor
        labels={"foo": "bar"},
        name="dgt_govil_dbt",
        task_id="run_job_on_dgt_govil_dbt",
        image_pull_policy="Always",
        get_logs=True,
        dag=dag
    )
    dbt_run.dry_run()
