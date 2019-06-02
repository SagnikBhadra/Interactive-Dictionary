import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def defin_of_word (word):
    word = word.lower()
    if  word in data:
        return data[word]
    elif get_close_matches(word, data.keys(), cutoff=0.8):
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "The word doesn't exist. Please double check it."

defin = defin_of_word(input("Enter word: "))
print(defin)
