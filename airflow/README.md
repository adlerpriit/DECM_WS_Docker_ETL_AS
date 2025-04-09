# AIRFLOW configuration

Before first spinning up airflow webserver or airflow standalone, you need to set environtment varianle
```bash
export AIRFLOW_HOME=$(pwd) # in this folder
```
or add this environmental variable to `devcontainer.json` file, as seen in this repository.

Then you can run airflow commands like:
```bash
airflow standalone
```

This will run apache airflow all-in-one and create required files, inlcuding `airflow.cfg`. By default airflow webserver wants to use port 8080, but as we have set up our apache superset on this port, we should change one of them. Also loading example DAGs might be confusing in the beginning.

Search and change the following lines in `airflow.cfg` file:

```
load_examples = False # by default True

web_server_port = 8081 # by default 8080
```

Now stop airflow by `ctrl-C` in the corresponding terminal window, remove `airflow.db` and then you can run `airflow standalone` again.

## Creating new DAGs