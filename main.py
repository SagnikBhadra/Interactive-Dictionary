import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def defin_of_word (word):
    word = word.lower()
    if  word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif get_close_matches(word, data.keys(), cutoff=0.8):
        yn =  input ("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

defin = defin_of_word(input("Enter word: "))

if type(defin) == list:
    for item in defin:
        print(item)
else:
    print(defin)
