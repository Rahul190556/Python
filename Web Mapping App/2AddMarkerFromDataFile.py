import pandas
import folium

data= pandas.read_csv("Web Mapping App/Volcanoes_USA.txt")
# print(data)
lat=list(data["LAT"]) #longitude
lon=list(data["LON"]) #Latitude

map = folium.Map(location=[38.58, -99.09],zoom_start=6,titles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")


for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Hi I am a Marker",icon=folium.Icon(color='orange')))


map.add_child(fg)
print(map)
map.save("Map2.html")


