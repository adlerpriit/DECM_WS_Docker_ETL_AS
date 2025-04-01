## Creating a new database connection in Superset with DuckDB

* Open your web browser and navigate to `localhost:8080`. This will take you to the Apache Superset login page.
* Enter the credentials you set up during the initialization process to log in.

Once logged in, follow these steps to connect to your data source:

1. Click on the '+' icon, then select 'Connect Database'.
2. In the 'Connect Database' screen, you'll see a 'Supported databases' dropdown menu. Select `DuckDB` from this list.
3. For the URI, you need to specify the location of your database. Enter `duckdb:////data/AirQuality.db` into the URI field.

By connecting to the DuckDB database, you're setting up Superset to directly query and visualize the data you've transformed and stored. DuckDB is an in-process SQL OLAP Database Management System, perfect for analytical queries on large datasets, like the air quality data we're working with.

To start visualizing the air quality data, we first need to create a dataset within Apache Superset. This dataset will be the foundation for our explorations and visualizations. Follow the steps below to create a dataset from the Parquet files we prepared earlier:

1. From the top navigation bar, select `SQL` and then `SQL Lab` from the dropdown menu. SQL Lab is a flexible tool within Superset that allows for executing SQL queries on your connected databases.
2. Within SQL Lab, you'll see an option to select your database. Choose the database connection you set up previously (the one connected to `DuckDB`).
3. In the SQL query editor that appears, you'll enter a SQL query to load your data. Type or copy the following SQL command into the editor:
    ```sql
    SELECT * FROM read_parquet('/data/parquet/*.parquet') ORDER BY DateTime;
    ```
    This SQL command tells Superset to read all Parquet files located in `/data/parquet/` and orders the resulting records by the `DateTime` column. Using the `read_parquet` function allows us to directly query and work with the Parquet files as if they were tables in a database, making it extremely convenient for analysis.
4. After entering the query, execute it by pressing the "Run selection" button. This action will load the data and display the results within SQL Lab. After confirming that the query works, save it as a dataset using the "Save" -> "Save dataset" button. Saving datasets allows you to reuse them across multiple visualizations without re-executing the query.

## Different views of the data

We can also create different virtual datasets for specific types of visualizations from the same underlying data. For example, the following query:

```sql
WITH DirectionBins AS (
    SELECT
        DateTime,
        WS10,
        CASE
            WHEN WD10 >= 337.5 OR WD10 < 22.5 THEN 'N'
            WHEN WD10 >= 22.5 AND WD10 < 67.5 THEN 'NE'
            WHEN WD10 >= 67.5 AND WD10 < 112.5 THEN 'E'
            WHEN WD10 >= 112.5 AND WD10 < 157.5 THEN 'SE'
            WHEN WD10 >= 157.5 AND WD10 < 202.5 THEN 'S'
            WHEN WD10 >= 202.5 AND WD10 < 247.5 THEN 'SW'
            WHEN WD10 >= 247.5 AND WD10 < 292.5 THEN 'W'
            WHEN WD10 >= 292.5 AND WD10 < 337.5 THEN 'NW'
            ELSE 'Unknown'
        END AS Direction
    FROM
        read_parquet('/data/parquet/*.parquet')
),
WindSpeed AS (
    SELECT
        DateTime,
        AVG(CASE WHEN Direction = 'N' THEN WS10 ELSE NULL END) AS N,
        AVG(CASE WHEN Direction = 'NE' THEN WS10 ELSE NULL END) AS NE,
        AVG(CASE WHEN Direction = 'E' THEN WS10 ELSE NULL END) AS E,
        AVG(CASE WHEN Direction = 'SE' THEN WS10 ELSE NULL END) AS SE,
        AVG(CASE WHEN Direction = 'S' THEN WS10 ELSE NULL END) AS S,
        AVG(CASE WHEN Direction = 'SW' THEN WS10 ELSE NULL END) AS SW,
        AVG(CASE WHEN Direction = 'W' THEN WS10 ELSE NULL END) AS W,
        AVG(CASE WHEN Direction = 'NW' THEN WS10 ELSE NULL END) AS NW
    FROM
        DirectionBins
    GROUP BY
        DateTime
)
SELECT * FROM WindSpeed;
```

This query creates a new dataset that calculates the average wind speed (`WS10`) for each wind direction (`N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`). The `WITH` clause is used to create temporary tables (CTEs) that help in organizing the data transformation process. The final `SELECT` statement retrieves the averages for each direction (although in our case the average is not strictly required, as each timestamp has only one value, `SQL` required grouping or summary function here in case that is not true).

## Hack for month name ordering

When visualizing data by month, the default alphabetical ordering of month names can be problematic. Use the following SQL snippet to enforce the correct chronological order:

```sql
CASE
WHEN monthname(DateTime) = 'January'   THEN '           Jan'
WHEN monthname(DateTime) = 'February'  THEN '          Feb'
WHEN monthname(DateTime) = 'March'     THEN '         Mar'
WHEN monthname(DateTime) = 'April'     THEN '        Apr'
WHEN monthname(DateTime) = 'May'       THEN '       May'
WHEN monthname(DateTime) = 'June'      THEN '      Jun'
WHEN monthname(DateTime) = 'July'      THEN '     Jul'
WHEN monthname(DateTime) = 'August'    THEN '    Aug'
WHEN monthname(DateTime) = 'September' THEN '   Sep'
WHEN monthname(DateTime) = 'October'   THEN '  Oct'
WHEN monthname(DateTime) = 'November'  THEN ' Nov'
WHEN monthname(DateTime) = 'December'  THEN 'Dec'
ELSE monthname(DateTime)
END
```

## Hack for day name ordering

Similarly, for visualizing data by day of the week, use this SQL snippet to ensure proper ordering:

```sql
CASE
WHEN dayname(DateTime) = 'Monday'    THEN '      Mon'
WHEN dayname(DateTime) = 'Tuesday'   THEN '     Tue'
WHEN dayname(DateTime) = 'Wednesday' THEN '    Wed'
WHEN dayname(DateTime) = 'Thursday'  THEN '   Thu'
WHEN dayname(DateTime) = 'Friday'    THEN '  Fri'
WHEN dayname(DateTime) = 'Saturday'  THEN ' Sat'
WHEN dayname(DateTime) = 'Sunday'    THEN 'Sun'
ELSE dayname(DateTime)
END
```

### Note:
The `CASE` statement in SQL is a powerful tool for conditional logic. It evaluates conditions in order and returns the corresponding value for the first condition that evaluates to `TRUE`. This is particularly useful for creating custom groupings or ordering in datasets.