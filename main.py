import json

data = json.load(open("data.json"))

def defin_of_word (word):
    if  word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it."

defin = defin_of_word(input("Enter word: "))
print(defin)
