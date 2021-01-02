from src.cams import load_cams
from src.era5 import load_era5
import sys
import yaml
import signal
import pandas as pd

def handler(signum, frame):
    raise Exception("Time exceeded!")

def download_data(source, name, variables, city, start_date, end_date, latitude, longitude):
    area = [latitude+1.0, longitude, latitude, longitude+1.0]
    monthly_dates = pd.date_range(start=start_date, end=end_date, freq='M')
    for month_end in monthly_dates:
        month_start = month_end.replace(day=1)
        date_range = f'{month_start.strftime("%Y-%m-%d")}/{month_end.strftime("%Y-%m-%d")}'
        file_name = f'{name}/{city}/{month_start.year:04d}{month_start.month:02d}.grib'
        while True:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(1200)
            try:
                if source == 'cams':
                    load_cams(file_name, variables, date_range, area)
                elif source == 'era5':
                    load_era5(file_name, variables, date_range, area)
                else:
                    print('Invalid source')
                    sys.exit()
                break
            except Exception as e:
                print(e)
                print("Trying again ...")
