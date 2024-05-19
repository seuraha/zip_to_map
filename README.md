# zip_to_map

## Overview
This library provides a function to plot the locations of zipcodes on a map using Basemap and pgeocode.

## Installation
```bash
pip install git+https://github.com/seuraha/zip_to_map.git
pip install -r requirements.txt
```

## Usage
```python
from zip_to_map import zipcode_to_map

zipcodes = ['90210', '10001', '30301']
zipcode_to_map(zipcodes, us_map=True)
```