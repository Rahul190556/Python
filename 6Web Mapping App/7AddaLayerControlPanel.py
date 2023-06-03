import pandas
import folium

data= pandas.read_csv("7Web Mapping App/Volcanoes_USA.txt")
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

fgv=folium.FeatureGroup(name="Volcanoes")

#elevation is float type so we have to into string first in right side of popup
for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"m",fill_color=color_producer(el),color="grey",fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

# #the recent version of Folium needs a string instead of a file as data input. Therefore you may need to add a read() method

with open("Web Mapping App/world.json", "r", encoding="utf-8-sig") as file:
        data = file.read()

fgp.add_child(folium.GeoJson(data=data,style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' 
                                                                   if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Web Mapping App/Map7.html")




