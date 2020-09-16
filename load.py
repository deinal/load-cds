import argparse
from src.cams import load_cams
from src.era5 import load_era5

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--all', action='store_true', help='load data from every source')
parser.add_argument('-c', '--cams', action='store_true', help='load cams data')
parser.add_argument('-e', '--era5', action='store_true', help='load era5 data')
args = parser.parse_args()

if args.all:
    load_cams()
    load_era5()
elif args.cams:
    load_cams()
elif args.era5:
    load_era5()