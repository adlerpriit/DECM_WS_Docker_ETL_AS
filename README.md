# DECM_WS_Docker_ETL_AS

This repository is designed to help students set up and use a development environment for ETL (Extract, Transform, Load) processes and data visualization using Apache Superset. Below are step-by-step instructions to guide you through the setup and usage.

---

## Setting up Apache Superset

Apache Superset is a powerful data visualization tool. To set it up, follow the detailed instructions in [superset_build/README.md](superset_build/README.md). 

### Quick Overview:
1. Navigate to the `superset_build` directory.
2. Follow the steps to build and run the Superset container.
3. Once running, access Superset at `http://localhost:8088` and log in using the credentials provided in the setup guide.

---

## Setting up the Development Container

The development container is configured using the `.devcontainer/devcontainer.json` file. It provides a pre-configured environment with all necessary dependencies.

### Steps:
1. Open this repository in VS Code.
2. Install the "Remote - Containers" extension if not already installed.
3. Reopen the repository in the development container:
   - Press `F1` in VS Code.
   - Select `Remote-Containers: Reopen in Container`.
4. The container will automatically install Python dependencies from [requirements.txt](requirements.txt).

For more details on Docker and development containers, refer to [docs/Docker_in_a_Nutshell.md](docs/Docker_in_a_Nutshell.md).

---

## Performing the ETL Process

The ETL process involves downloading, transforming, and preparing data for analysis. Below are the steps to perform ETL using the provided Python scripts.

### Step 1: Download Data
Run the following command to download air quality data:
```bash
python3 download_AirQuality.py 8 2024 2024
```
This will download data about Tartu for 2024.

### Step 2: Transform Data
Transform the downloaded CSV files into `Parquet` format:
```bash
for fn in $(ls data/csv); do 
    echo "Transforming $fn..."; 
    python3 transform_AirQuality.py data/csv/$fn data/parquet/$(basename $fn .csv).parquet; 
done;
```

### Step 3: Additional Transformations
If you also downloaded data from Ilmateenistus and fixed the immidiate issues in the Excel file, you can run the following command to transform it into `Parquet` format:
```bash
python3 transform_ilmateenistus.py
```

### Step 4: Load Data into Superset
Once the data is prepared, you can load it into Apache Superset for visualization. Refer to [docs/Superset_snippets.md](docs/Superset_snippets.md) for SQL snippets and tips.

---

## Additional Documentation

- [docs/Docker_in_a_Nutshell.md](docs/Docker_in_a_Nutshell.md): A quick guide to Docker basics.
- [docs/VSCode_Git_Github.md](docs/VSCode_Git_Github.md): Tips for using VS Code, Git, and GitHub effectively.
- [docs/Superset_snippets.md](docs/Superset_snippets.md): Useful SQL snippets and tips for working with Apache Superset.

---

This repository is designed to be a hands-on resource. Feel free to explore the scripts and customize them to suit your needs. Happy learning!
