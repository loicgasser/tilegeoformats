import os
import sys
import json
import cStringIO
import mapbox_vector_tile
from shapely.geometry import shape


def is_bounds2d(bounds):
    if len(bounds) != 4 or bounds[0] > bounds[2] or bounds[1] > bounds[3]:
        return False
    return True


def read_geojson(geojson_file):
    with open(geojson_file, 'r') as f:
        geojson_obj = json.load(f)
    return geojson_obj


def to_layer_mvt(features, bounds, layer_name='foo'):
    return mapbox_vector_tile.encode({
        'name': layer_name,
        'features': features,
    }, quantize_bounds=bounds)


def to_feature_mvt(geometry, properties):
    return {
        'geometry': geometry,
        'properties': properties
    }


def get_filename(geojson_file):
    paths = geojson_file.split('/')
    file_name = paths[len(paths) - 1]
    return file_name.split('.json')[0]


def to_pbf(mvt_file, mvt_tile):
    with open(mvt_file, 'wb') as f:
        f.write(mvt_tile)


def main():
    if len(sys.argv) < 3:
        print 'Please provide a geojson and an extent'
        sys.exit(1)
    geojson_file = sys.argv[1]
    if not os.path.exists(geojson_file):
        print 'Geojson file %s does not exists' % geojson_file
    bounds = [float(c) for c in sys.argv[2].split(',')]
    if not is_bounds2d(bounds):
        print 'Please provide a valid bbox'
        print 'Bottom left to top right only'
        sys.exit(1)

    try:
        data = read_geojson(geojson_file) 
    except Exception as e:
        raise Exception(e)

    if len(data['features']) > 0:
        features_mvt = []
        features = data['features']
        for feature in features:
            geometry = shape(feature['geometry'])
            properties = feature['properties'] if 'properties' in feature else {}
            features_mvt.append(to_feature_mvt(geometry, properties))
        mvt_tile = to_layer_mvt(features_mvt, bounds)
    else:
        print 'Empty geojson file'
        sys.exit(1) 

    mvt_file = 'mvts/%s.pbf' % get_filename(geojson_file)
    to_pbf(mvt_file, mvt_tile)


if __name__ == '__main__':
    main()
