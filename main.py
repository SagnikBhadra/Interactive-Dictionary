import json

data = json.load(open("data.json"))

def defin_of_word (word):
    return data[word]

defin = defin_of_word(input("Enter word: "))
print(defin)
