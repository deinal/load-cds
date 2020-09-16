
# load-cds

---

Load data from Climate and Atmosphere Data Store

---

## Set up APIs

### Climate Data Store

https://cds.climate.copernicus.eu/api-how-to

Put keys in `.cdsapi`:

```
url: https://cds.climate.copernicus.eu/api/v2
key: {uid}:{api-key}
```

### Atmosphere Data Store

https://ads.atmosphere.copernicus.eu/api-how-to

Put keys in `.adsapi`:

```
url: https://ads.atmosphere.copernicus.eu/api/v2
key: {uid}:{api-key}
```

## Run

Load from every source
```
python load.py --all
```
Load cams data
```
python load.py --cams
```
Load era5 data
```
python load.py --era5
```

## Install dependencies

Using pip
```
pip install -r requirements.txt
```
or using conda
```
conda install --file requirements.txt
```

## Specify data

Modify the requests e.g.

```
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
'data/cams/test.grib'
```

in `src/cams.py` or `src/era5.py` according to your need, this process is preferrably automated.

More info on

1. https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-reanalysis-eac4?tab=form
2. https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form

Plus from the multiple other datasets on Climate and Atmosphere Data Store, they provide example API requests at the bottom of the pages.