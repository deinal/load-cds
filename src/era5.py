import cdsapi
import yaml

def load_era5():
    with open('.cdsapi', 'r') as f:
            credentials = yaml.safe_load(f)

    c = cdsapi.Client(url=credentials['url'], key=credentials['key'])

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'variable': 'boundary_layer_height',
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
        'data/era5/test.grib')