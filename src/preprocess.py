
from src.util import concat_files, listdir_fullpath
import xarray as xr

def preprocess_data(name, city, latitude, longitude, set_positive_longitude):
   """
      Create csv files from GRIB files.
   """
   given_longitude = longitude
   if longitude < 0 and set_positive_longitude: longitude = longitude + 360
   files = listdir_fullpath(f'raw/{name}/{city}')
   files = [f for f in files if ('.idx' not in f) and (f'{city}.grib' not in f)]
   outgrib = f'raw/{name}/{city}/{city}.grib'
   concat_files(files, outgrib)
   ds = xr.open_dataset(outgrib, engine='cfgrib')
   df = ds.loc[dict(latitude=latitude, longitude=longitude)].to_dataframe()
   df = df.groupby(df.index.date).mean()
   df.longitude = given_longitude
   df.index.name = 'date'
   df.to_csv(f'data/{name}/{city}.csv')
