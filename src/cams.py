
import cdsapi
import yaml

def load_cams():
    with open('.adsapi', 'r') as f:
            credentials = yaml.safe_load(f)

    c = cdsapi.Client(url=credentials['url'], key=credentials['key'])

    c.retrieve(
        'cams-global-reanalysis-eac4',
        {
            'format': 'grib',
            'model_level': '60',
            'variable': [
                'carbon_monoxide', 'temperature',
            ],
            'date': '2018-05-01/2018-06-01',
            'time': [
                '00:00', '03:00', '06:00',
                '09:00', '12:00', '15:00',
                '18:00', '21:00',
            ],
            'area': [
                22, 5, 20, 6,
            ],
        },
        'data/cams/test.grib')