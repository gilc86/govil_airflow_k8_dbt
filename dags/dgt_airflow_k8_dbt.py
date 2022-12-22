from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
DBT_DIR = './dbt/dgt_govil_dbt'
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
        tags=['1.0.1']
) as dag:
    dbt_run = KubernetesPodOperator(
        namespace="k8-executor",  # the new namespace you've created in the Workload Identity creation process
        service_account_name="composer1", # the new k8 service account you've created in the Workload Identity creation process
        image="eu.gcr.io/dgt-gcp-egov-test-govilbi-0/dgt_govil_dbt@sha256:86566482d4abf1207d97c2388ccb770a2d86eba31d57046847372d5458abccb8",
        # startup_timeout_seconds=500,
        cmds=["bash", "-cx"],
        # arguments=["cd" , "./dbt/dgt_govil_dbt" , "&& dbt run"], #Liad & Oded
        arguments=["cd /home/dbtuser/dgt_govil_dbt && dbt run"], #Leedor
        # arguments=["cd /home/dbtuser/dgt_govil_dbt ", "&& dbt run"], #Gil & Yoel
        # arguments=["ll"], #Gil & Yoel
        # arguments=["cd './dbt/dgt_govil_dbt' && dbt run"],
        labels={"foo": "bar"},
        name="dgt_govil_dbt",
        task_id="run_job_on_dgt_govil_dbt",
        image_pull_policy="Always",
        get_logs=True,
        dag=dag
    )

    dbt_run.dry_run()
