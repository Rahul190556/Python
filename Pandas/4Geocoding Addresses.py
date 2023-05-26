from geopy.geocoders import Nominatim
import pandas as pd
df = pd.read_csv("Pandas/supermarkets.csv")

nom = Nominatim(user_agent="http://pythonhow.com/supermarkets.json")
location = nom.geocode("3995 23rd Street, San Francisco, CA 94114")

# if location is not None:
#     print("Latitude:", location.latitude)
#     print("Longitude:", location.longitude)
# else:
#     print("Location not found.")

df["Address"]=df["Address"] + "," + df["City"] + "," + df["State"] + "," + df["Country"]
print(df,'\n')

df["Coordinates"]=df["Address"].apply(nom.geocode)
print(df,'\n')
print(df.Coordinates[0],'\n')

df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x!=None else None) # if there is no latitude exist then it will assign to that row by none
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x!=None else None)
print(df,'\n')