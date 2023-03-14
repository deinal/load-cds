import cdsapi
import yaml
import urllib3
from datetime import datetime, timedelta

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


with open('.adsapi', 'r') as f:
    credentials = yaml.safe_load(f)

c = cdsapi.Client(url=credentials['url'], key=credentials['key'])

start_date = datetime(2022, 5, 1)
end_date = datetime(2022, 5, 31)
delta = timedelta(days=1)

while start_date <= end_date:
    current_date = str(start_date.date())
    c.retrieve(
        'cams-global-reanalysis-eac4',
        {
            'format': 'grib',
            'model_level': '60',
            'variable': [
                'carbon_monoxide', 'isoprene', 'nitrogen_dioxide', 
                'nitrogen_monoxide', 'sulphur_dioxide'
            ],
            'date': current_date,
            'time': [
                '00:00', '03:00', '06:00',
                '09:00', '12:00', '15:00',
                '18:00', '21:00',
            ],
        },
        f'global/{current_date}.grib')

    start_date += delta