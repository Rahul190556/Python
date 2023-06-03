import json
from difflib import get_close_matches

data = json.load(open("3BuildingDictionary/data.json"))


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
            for i in range(1,5):
               yn1=input( "Did you mean %s instead? Enter Y if yes, or N if no:" % get_close_matches(w,data.keys(),n=5)[i])
               if yn1=="Y":
                 return data[get_close_matches(w, data.keys())[i]]
               elif yn1=="N":
                    continue
               else:
                    return "we didn't understand your entry"
            return "Word is not found.Please double check it"
        else:
            return "we didn't understand your entry"

    else:
        return "Word is not found.Please double check it"


word = input("Enter word:")

output = translate(word)

if (
    type(output) == list
):                        # If we not write this condition then whenver o/p not match in dictionary
    for item in output:   # then it will seperated character of word that it is not found
        print(item)
else:
    print(output)
