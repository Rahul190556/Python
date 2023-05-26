"""JSON is perfect for storing temporary data. For example,temporary data
    can be user-generated data, such as a submitted form on a website.
   JSON can also be used as a data format for any programming language to provide 
   a high level of interoperability.Json file is similar to python dictionary"""

import json

data = json.load(open("BuildingDic/data.json"))

print(type(data))
print(data["rain"])
