# loading districts
INPUT_FILE = './districts.txt'
ortsfile = open(INPUT_FILE)
ortsdata = ortsfile.read().splitlines() 

# saving js code
OUTPUT_FILE = 'districts.js'
districtsfile = open(OUTPUT_FILE, 'a')

# generate JavaScript code
for ort in ortsdata:
   js = '''
        const %s = new google.maps.Polygon({
          paths: %sCoords,
          strokeColor: "#000000",
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: "#000000",
          fillOpacity: 0.5,
        });
        // %s.setMap(map);
        ''' % (ort, ort, ort)
   districtsfile.write(js) 
