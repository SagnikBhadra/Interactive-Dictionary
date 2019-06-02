import json

def defin_of_word (word, data):
    return data[word]

data = json.load(open("data.json"))
defin = defin_of_word(input("Enter word: "), data)
print(defin)
