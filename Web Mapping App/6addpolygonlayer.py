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
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(el)+"m",fill_color=color_producer(el),color="grey",fill_opacity=0.7))



# #the recent version of Folium needs a string instead of a file as data input. Therefore you may need to add a read() method

try:
    with open("Web Mapping App/world.json", "r", encoding="utf-8-sig") as file:
        data = file.read()

    fg.add_child(folium.GeoJson(data=data,style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' 
                                                                   if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))


    map.add_child(fg)

    # Save or display the map
    map.save("Web Mapping App/Map6.html")
    # map_obj.show()  # Uncomment this line if you want to display the map directly

    print("Map created successfully!")
except FileNotFoundError:
    print("The 'world.json' file was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")




