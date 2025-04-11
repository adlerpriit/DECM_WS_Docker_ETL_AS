# Apache Airflow Configuration

Before starting the Airflow webserver or running Airflow in standalone mode for the first time, you need to set the `AIRFLOW_HOME` environment variable. This variable specifies the directory where Airflow will store its configuration and metadata.

To set the environment variable temporarily, run the following command in your terminal:

```bash
export AIRFLOW_HOME=$(pwd) # Set to the current folder
```

Alternatively, you can add this environment variable to the `devcontainer.json` file in this repository for a persistent setup.

Once the environment variable is set, you can run Airflow commands like:

```bash
airflow standalone
```

This command will start Apache Airflow in standalone mode, which includes the webserver, scheduler, and other components. It will also create the required files, including `airflow.cfg`. 

By default, the Airflow webserver uses port `8080`. However, since this repository has Apache Superset configured (see [Superset README](../superset_build/README.md)) to use the same port, you need to change one of them to avoid conflicts. Additionally, loading example DAGs might be unnecessary and confusing for beginners.

To make these changes, open the `airflow.cfg` file and update the following lines:

```ini
load_examples = False # Disable loading example DAGs (default is True)

web_server_port = 8081 # Change the webserver port to 8081 (default is 8080)
```

After making these changes, stop Airflow by pressing `Ctrl+C` in the terminal where it is running. Then, delete the `airflow.db` file (the default SQLite database) to reset the metadata. Finally, restart Airflow using the `airflow standalone` command.

---

## Creating New DAGs

A Directed Acyclic Graph (DAG) in Airflow defines a workflow as a collection of tasks and their dependencies. Below is an example of how to create a simple DAG that downloads data from a URL.

### Example: Downloading Data with a DAG

Create a new Python file in the `dags` (you may need to first create the `dags` folder to the same folder with `airflow.cfg` file) folder (e.g., `download_data.py`) and add the following code:

```python
from airflow.decorators import dag, task
import datetime
import requests
import logging

@dag(
    dag_id="example_download_data",
    start_date=datetime.datetime(2023, 1, 1),
    schedule="0 12 * * *",  # Runs daily at 12:00 PM
    catchup=False
)
def download_data_workflow():
    """
    A simple DAG that downloads data from a URL daily at 12:00 PM.
    """

    @task
    def download_data():
        url = "https://example.com/data.csv"
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open('/path/to/save/data.csv', 'w') as f:
                f.write(response.text)
            logging.info("Data downloaded successfully!")
        except Exception as e:
            logging.error(f"Failed to download data: {str(e)}")
            raise

    download_data()

example_dag = download_data_workflow()
```

### Steps to Add a New DAG

1. Save the Python file in the `dags` folder.
2. Restart the Airflow webserver to load the new DAG.
3. Open the Airflow web interface (default: `http://localhost:8081`) and enable the DAG from the DAGs list.

This example demonstrates how to define a simple workflow. You can expand it by adding more tasks and dependencies as needed.

---

For more information, refer to the [Apache Airflow documentation](https://airflow.apache.org/docs/).