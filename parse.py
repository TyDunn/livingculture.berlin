import json
from pyreproj import Reprojector

# defining projection
rp = Reprojector()
transform = rp.get_transformation_function(from_srs='epsg:25833', to_srs=4326)

# defining output files
coords = open("coords.json", "a")
districts = open("districts.json", "a")

# loading EPSG25833 data
INPUT_FILE = './ortsteil.json'
ortsfile = open(INPUT_FILE)
ortsdata = json.load(ortsfile)

# Example of JSON access
# mitte_name = ortsdata['FeatureCollection']['featureMember'][0]['re_ortsteil']['spatial_alias']['__text']
# mitte_loc = ortsdata['FeatureCollection']['featureMember'][0]['re_ortsteil']['spatial_geometry']['Polygon']['exterior']['LinearRing']['posList']['__text']

# Example projection
# mitte_loc_lst = mitte_loc.split()
# mitte_loc_pairs = [mitte_loc_lst[i:i+2] for i in range(0,len(mitte_loc_lst),2)]
# for i in mitte_loc_pairs:
#    lat_lng = transform(i[0], i[1])
#    print("{ lat: " + str(lat_lng[0]) + ", lng: " + str(lat_lng[1]) + " },")

for ortsteil in ortsdata['FeatureCollection']['featureMember']:
    name = ortsteil['re_ortsteil']['spatial_alias']['__text']
    districts.write(name + ",\n")
    coords.write("// " + name + "\n")
    coords.write(name + "Coords = [\n")
    try:
        ortsteil['re_ortsteil']['spatial_geometry']['MultiSurface']
    except KeyError:
        loc = ortsteil['re_ortsteil']['spatial_geometry']['Polygon']['exterior']['LinearRing']['posList']['__text']
    else: 
        loc = ortsteil['re_ortsteil']['spatial_geometry']['MultiSurface']['surfaceMember'][0]['Polygon']['exterior']['LinearRing']['posList']['__text'] 
    loc_lst = loc.split()
    loc_pairs = [loc_lst[i:i+2] for i in range(0,len(loc_lst),2)] 
    for i in loc_pairs:
        lat_lng = transform(i[0], i[1])
        coords.write("  { lat: " + str(lat_lng[0]) + ", lng: " + str(lat_lng[1]) + " },\n")
    coords.write("];\n\n")
   
ortsfile.close()
coords.close()
