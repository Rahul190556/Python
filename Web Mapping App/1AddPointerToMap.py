import folium
# print(dir(folium))
# help(folium)/
# Create a map centered at New York City
map = folium.Map(location=[38.58, -99.09],zoom_start=6,titles="Mapbox Bright")
# map.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green'))) ->this is bad method to mark at map
#feature group helps to organize the map in efficient manner
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hi I am a Marker",icon=folium.Icon(color='green')))


#adding multiple mark using for loop
for coordinates in [[40.2,-99.1],[39.2,-97.1]]:
    fg.add_child(folium.Marker(location=coordinates,popup="Hi I am a Marker",icon=folium.Icon(color='orange')))


map.add_child(fg)
print(map)
map.save("Map1.html")


