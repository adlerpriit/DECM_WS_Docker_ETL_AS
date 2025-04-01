import requests
import datetime
import argparse

# Define command line arguments for station ID, year start, and year end
parser = argparse.ArgumentParser(description='Fetch air quality data from airviro.klab.ee')
parser.add_argument('station_id', type=int, default=8, help='The station ID to fetch data for')
parser.add_argument('start', type=int, help='The start year to fetch data for')
parser.add_argument('stop', type=int, help='The end year to fetch data for (included)')
args = parser.parse_args()

def fetch_air_range(station_id, date_from, date_until):
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
    response = requests.post(url, data)

    # Return the text content of the response
    return response.text

def get_first_and_last_day_of_month(year, month):
    # Calculate the first and last day of the month
    first_day = datetime.date(year, month, 1)
    if month == 12:
        num_days = 31
    else:
        num_days = (datetime.date(year, month+1, 1) - datetime.timedelta(days=1)).day
    last_day = datetime.date(year, month, num_days)
    return first_day, last_day

def fetch_air_year(station_id, year):
    # Fetch monthly results within a year
    for month in range(1, 13):
        first_day, last_day = get_first_and_last_day_of_month(year, month)
        print(f'Fetching data from {first_day} to {last_day}, included')
        monthdata = fetch_air_range(station_id, first_day, last_day)
        with open(f'csv/air_{station_id}_{year}_{month}.csv', 'w') as f:
            f.write(monthdata)

for year in range(args.start, args.stop+1):
    print(f'Fetching data for year {year}')
    fetch_air_year(args.station_id, year)