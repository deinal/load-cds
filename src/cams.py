import cdsapi
import yaml
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_cams(file_name, variables, date_range, area):
    with open('.adsapi', 'r') as f:
        credentials = yaml.safe_load(f)

    c = cdsapi.Client(url=credentials['url'], key=credentials['key'])

    c.retrieve(
        'cams-global-reanalysis-eac4',
        {
            'format': 'grib',
            'model_level': '60',
            'variable': variables,
            'date': date_range,
            'time': ['00:00', '06:00', '12:00', '18:00'],
            'area': area,
        },
        f'raw/{file_name}')
