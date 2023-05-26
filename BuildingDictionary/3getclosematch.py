# SequenceMatcher is a class that is available in the difflib Python package. The difflib module provides classes
# and functions for comparing sequences.

import json
import difflib

data = json.load(open("BuildingDic/data.json"))
from difflib import SequenceMatcher
from difflib import get_close_matches

print(SequenceMatcher(None, "rainn", "rain"))
print(get_close_matches("rainn", data.keys()))  # ['rain', 'train', 'rainy']
print(
    get_close_matches("rainn", data.keys(), n=6)
)  # it will give six similarities starting from higher priority ['rain', 'train', 'rainy', 'grain', 'drain', 'brain']
print(
    get_close_matches("rainn", data.keys())[0]
)  # it will give higher priority matches o/p: rain
