import json

data = json.load(open("BuildingDic/data.json"))


def translate(w):
    w = w.lower()  # we use this so that we our program became case insensitive
    if w in data:
        return data[w]
    else:
        print("Word is not found.Please double check it")


word = input("Enter word:")

print(translate(word))
