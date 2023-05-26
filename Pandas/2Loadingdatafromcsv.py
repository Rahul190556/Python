import pandas as pd

df1 = pd.read_csv("Pandas/supermarkets.csv")
# df1.shape it gives order of data frames like 6 X 7
df2 = pd.read_json("Pandas/supermarkets.json")
df3=pd.read_json("http://pythonhow.com/supermarkets.json")  #reading data from url


print(df1,'\n')
print(df2,'\n')
print(df3.set_index("Address"))

 #slicing & indexing data frames
print(list(df3.loc[:,"Country"]),'\n')
print(df3.iloc[1:3,1:4],'\n')
print(df3.iloc[3,1:4])

#deleting
print(df3.drop(index=0,columns="City") )

