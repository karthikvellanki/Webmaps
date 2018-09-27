import folium

import pandas

data = pandas.read_csv("Volcanoes_USA.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def iconcolor(elevation):
	if elevation < 2000:
		return "green"
	else:
		return "blue"

map = folium.Map(location=[43, -116], zoom_start=4, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
	fgv.add_child(folium.CircleMarker(location=[lt, ln], popup="Elevation: "+ str(el) +" m", radius=7, fill_color=iconcolor(el), color="grey", opacity=0.7))

fgpop = folium.FeatureGroup(name="Population Data")

fgpop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005'] < 50000000
else 'orange' if 50000000<=x['properties']['POP2005']<100000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgpop)

map.add_child(folium.LayerControl())

map.save("WebMap.html")