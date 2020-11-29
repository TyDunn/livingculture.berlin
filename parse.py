import json
from pyreproj import Reprojector

# defining projection
rp = Reprojector()
transform = rp.get_transformation_function(from_srs='epsg:25833', to_srs=4326)

# loading EPSG25833 data
INPUT_FILE = './ortsteil.json'
ortsfile = open(INPUT_FILE)
ortsdata = json.load(ortsfile)

# Example of JSON access
mitte_name = ortsdata['FeatureCollection']['featureMember'][0]['re_ortsteil']['spatial_alias']['__text']
mitte_loc = ortsdata['FeatureCollection']['featureMember'][0]['re_ortsteil']['spatial_geometry']['Polygon']['exterior']['LinearRing']['posList']['__text']

mitte_loc_lst = mitte_loc.split()
mitte_loc_pairs = [mitte_loc_lst[i:i+2] for i in range(0,len(mitte_loc_lst),2)]

for i in mitte_loc_pairs:
    lat_lng = transform(i[0], i[1])
    print("{ lat: " + str(lat_lng[0]) + ", lng: " + str(lat_lng[1]) + " },")

# for ortsteil in ortsdata['FeatureCollection']['featureMember']:
#    print(ortsteil['re_ortsteil']['spatial_alias']['__text'])

ortsfile.close()
