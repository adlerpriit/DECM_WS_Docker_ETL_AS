with csv_data as (
    select 
        CAST(Kuupäev as DATETIME) as "DateTime",
        SO2,
        NO2,
        CO,
        O3,
        PM10,
        "PM2.5" as "PM2p5",
        TEMP,
        WD10,
        WS10
    from read_csv('/workspaces/DECM_WS_Docker_ETL_AS/data/csv/*.csv', decimal_separator = ',', delim = ';', header = true)
)

select * 
from csv_data