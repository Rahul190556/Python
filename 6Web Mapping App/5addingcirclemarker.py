import pandas
import folium

data= pandas.read_csv("6Web Mapping App/Volcanoes_USA.txt")
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
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"m",fill_color=color_producer(el),color="grey",fill_opacity=0.7))


map.add_child(fg)
print(map)
map.save("Map5.html")


