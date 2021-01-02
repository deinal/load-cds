
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

Specify requests in `main.py` and execute it.

## Install dependencies

Using pip
```
pip install -r requirements.txt
```
or using conda
```
conda install -c conda-forge --file requirements.txt
```

## Data sources

1. https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-reanalysis-eac4?tab=form
2. https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form

## Documentation

Variable explanations etc.

1. https://confluence.ecmwf.int/display/CKB/CAMS%3A+Reanalysis+data+documentation
2. https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation
