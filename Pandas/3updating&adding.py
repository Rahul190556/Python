import pandas as pd

df1 = pd.read_csv("Pandas/supermarkets.csv")
# df1.shape it gives order of data frames like 6 X 7
df2 = pd.read_json("Pandas/supermarkets.json")
df3=pd.read_json("http://pythonhow.com/supermarkets.json")  #reading data from url
df3=df3.set_index("Address")
df3["Continent"]=df3.shape[0]*["North America"]
print(df3,'\n')
df3["Continent"]=df3["Country"] + "," + df3.shape[0]*["North America"] #it will update Country name in continent column with its continent
print(df3,'\n')

df3T=df3.T # it will give transpose of df3 
print(df3T,'\n')
df3T["My Address"]=["My City","My Country",10,7,"My Shop","My State","My Continent"]
print(df3T,'\n')
df3=df3T.T
print(df3)