import pandas
import folium

data= pandas.read_csv("Web Mapping App/Volcanoes_USA.txt")
# print(data)
lat=list(data["LAT"]) #longitude
lon=list(data["LON"]) #Latitude
elev=list(data["ELEV"]) #elevation

def color_producer(elevation):
    if elevation < 1500:
      return 'green'
    elif 1500<=elevation<=3000:
       return 'orange'
    else:
       return 'red'

map = folium.Map(location=[38.58, -99.09],zoom_start=6,titles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")

#elevation is float type so we have to into string first in right side of popup
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color=color_producer(el))))


map.add_child(fg)
print(map)
map.save("Map4.html")


