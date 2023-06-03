import pandas
import folium

data= pandas.read_csv("6Web Mapping App/Volcanoes_USA.txt")
# print(data)
lat=list(data["LAT"]) #longitude
lon=list(data["LON"]) #Latitude
elev=list(data["ELEV"]) #elevation

map = folium.Map(location=[38.58, -99.09],zoom_start=6,titles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")

#elevation is float type so we have to into string first in right side of popup
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color='orange')))


map.add_child(fg)
print(map)
map.save("Map3.html")


