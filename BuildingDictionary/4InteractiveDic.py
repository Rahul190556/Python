import json
from difflib import get_close_matches

data = json.load(open("BuildingDic/data.json"))


def translate(w):
    w = w.lower()  # we use this so that we our program became case insensitive
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no:"
            % get_close_matches(w, data.keys())[0]
        )
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "Word is not found.Please double check it"
        else:
            return "we didn't understand your entry"

    else:
        print("Word is not found.Please double check it")


word = input("Enter word:")

print(translate(word))

# our output is not user friendly. now let us make our output user friendly in next program
