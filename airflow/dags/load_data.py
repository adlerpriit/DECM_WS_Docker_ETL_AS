from airflow.decorators import dag, task
import datetime
import requests
import logging

def get_first_last_day_of_the_month():
    today = datetime.date.today()
    first_of_month = today.replace(day=1)
    last_of_month = today.replace(day=31)
    return first_of_month, last_of_month

@dag(
    dag_id="download_airQ",
    start_date=datetime.datetime(2023, 1, 1),
    schedule_interval="20 * * * *",
    catchup=False
)
def my_data_download():
    """
    A DAG that downloads CSV data from airviro.klab.ee once every hour,
    with a 20-minute offset, to accommodate the ~10–20 minute data lag.
    """

    @task
    def download_csv(station_id=8):

        year = datetime.date.today().year
        month = datetime.date.today().month
        date_from = datetime.date(year, month, 1)
        date_until = (date_from.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) + datetime.timedelta(days=-1)
        # date_from, date_until = get_first_last_day_of_the_month()
        # Define the URL of the endpoint that provides the air quality data
        url = 'http://airviro.klab.ee/station/csv'

        # Define the parameters for the POST request
        data = {
            'filter[type]': 'INDICATOR',
            'filter[cancelSearch]': '',
            'filter[stationId]': station_id,
            'filter[dateFrom]': date_from,
            'filter[dateUntil]': date_until,
            'filter[submitHit]': '1',
            'filter[indicatorIds]': ''
        }

        # Send a POST request to the endpoint
        try:
            response = requests.post(url, data)
            response.raise_for_status()
            with open(f'/workspaces/DECM_WS_Docker_ETL_AS/data/csv/air_{station_id}_{year}_{month}.csv', 'w') as f:
                f.write(response.text)
            logging.info(f"Downloading current month data successful!")
        except Exception as e:
            logging.error(f"Error downloading CSV: {str(e)}")
            raise
    
    download_csv()

my_dag = my_data_download()