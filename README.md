### Install

  make all

### Convert a geojson tile to a mapbox vector tile

  .venv/bin/python scripts/geojsontile_to_mvttile.py geojsons/tile_sample.json 0,0,100,100

### Convert a geojson tile to a topojson tile

  node_modules/.bin/topojson -o topojsons/tile_sample.json --cartesian geojsons/tile_sample.json

In order to know which options are available for topojson please refer to https://github.com/mbostock/topojson/wiki/Command-Line-Reference
