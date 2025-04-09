from cosmos import DbtDag, ProjectConfig, ProfileConfig
from datetime import datetime

profile_config = ProfileConfig(
    profile_name="dbt_airQ",
    target_name="dev",
    profiles_yml_filepath="/workspaces/DECM_WS_Docker_ETL_AS/dbt_airQ/profiles.yml"
)

my_cosmos_dag = DbtDag(
    project_config=ProjectConfig(
        "/workspaces/DECM_WS_Docker_ETL_AS/dbt_airQ",
    ),
    profile_config=profile_config,
    # normal dag parameters
    schedule_interval="30 * * * *",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="my_cosmos_dag",
    default_args={"retries": 2},
)

# Airflow will parse this as your DAG
dag = my_cosmos_dag