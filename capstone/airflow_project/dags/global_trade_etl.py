from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from datetime import datetime

with DAG(
    dag_id="global_trade_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={"retries": 1},
) as dag:

    bronze = DatabricksSubmitRunOperator(
        task_id="capstone_bronze",
        databricks_conn_id="databricks_default",
        existing_cluster_id="0106-195339-tj02a9ds",
        notebook_task={
            "notebook_path": "/Workspace/Users/shivam.motwani2022@vitstudent.ac.in/Drafts/capstone_bronze"
        },
    )

    silver = DatabricksSubmitRunOperator(
        task_id="capstone_silver",
        databricks_conn_id="databricks_default",
        existing_cluster_id="0106-195339-tj02a9ds",
        notebook_task={
            "notebook_path": "/Workspace/Users/shivam.motwani2022@vitstudent.ac.in/Drafts/capstone_silver"
        },
    )

    gold = DatabricksSubmitRunOperator(
        task_id="capstone_gold",
        databricks_conn_id="databricks_default",
        existing_cluster_id="0106-195339-tj02a9ds",
        notebook_task={
            "notebook_path": "/Workspace/Users/shivam.motwani2022@vitstudent.ac.in/Drafts/capstone_gold"
        },
    )

    forecasting = DatabricksSubmitRunOperator(
        task_id="capstone_forecasting",
        databricks_conn_id="databricks_default",
        existing_cluster_id="0106-195339-tj02a9ds",
        notebook_task={
            "notebook_path": "/Workspace/Users/shivam.motwani2022@vitstudent.ac.in/Drafts/capstone_forcasting"
        },
    )

    emerging = DatabricksSubmitRunOperator(
        task_id="capstone_emerging_markets",
        databricks_conn_id="databricks_default",
        existing_cluster_id="0106-195339-tj02a9ds",
        notebook_task={
            "notebook_path": "/Workspace/Users/shivam.motwani2022@vitstudent.ac.in/Drafts/capstone_emerging_markets"
        },
    )

    bronze >> silver >> gold >> [forecasting, emerging]
