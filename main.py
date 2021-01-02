from src.util import make_directory
from src.download_data import download_data
from src.preprocess import preprocess_data
import pandas as pd

def request(source, name, variables, set_positive_longitude=True):
    cities_info = pd.read_csv('cities_info.csv')

    for _, row in cities_info.iterrows():
        make_directory(f'raw/{name}/{row["city"]}')
        download_data(source, name, variables, row['city'], row['start_date'], row['end_date'], row['latitude'], row['longitude'])

    for _, row in cities_info.iterrows():
        make_directory(f'data/{name}')
        preprocess_data(name, row['city'], row['latitude'], row['longitude'], set_positive_longitude)

if __name__ == '__main__':  
    request(source='cams', name='aerosols', set_positive_longitude=True, variables=[
        'dust_aerosol_0.03-0.55um_mixing_ratio', 'dust_aerosol_0.55-0.9um_mixing_ratio', 'dust_aerosol_0.9-20um_mixing_ratio',
        'hydrophilic_black_carbon_aerosol_mixing_ratio', 'hydrophobic_black_carbon_aerosol_mixing_ratio',
        'hydrophilic_organic_matter_aerosol_mixing_ratio', 'hydrophobic_organic_matter_aerosol_mixing_ratio', 
        'sea_salt_aerosol_0.03-0.5um_mixing_ratio', 'sea_salt_aerosol_0.5-5um_mixing_ratio', 'sea_salt_aerosol_5-20um_mixing_ratio', 
        'sulphate_aerosol_mixing_ratio'
    ])

    request(source='cams', name='gases', set_positive_longitude=True, variables=[
        'carbon_monoxide', 'isoprene', 'nitrogen_dioxide', 'nitrogen_monoxide', 'sulphur_dioxide'
    ])

    request(source='cams', name='atmospheric', set_positive_longitude=False, variables=[
        '2m_dewpoint_temperature', '2m_temperature'
    ])

    request(source='era5', name='boundary_layer_height', set_positive_longitude=False, variables=[
        'boundary_layer_height'
    ])

    request(source='cams', name='slow_access', set_positive_longitude=True, variables=[
        'ammonia', 'relative_humidity', 'specific_rain_water_content', 'terpenes'
    ])