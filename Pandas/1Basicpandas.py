import pandas
dataframe1=pandas.DataFrame([[2,4,6],[3,8,4]]) # dataframe is datastructure and it is like table
print(dataframe1)

df2=pandas.DataFrame([[2,4,6],[3,8,4]],columns=["price","Age","value"],index=["First","Second"])
print(df2)

df3 = pandas.DataFrame([{"Name": "Jhon", "Age": 23}, {"Name": "Rohit", "Age": 24}])
print(df3)
print(dataframe1.mean())  
print(df2.price)
# print(dir(dataframe1))