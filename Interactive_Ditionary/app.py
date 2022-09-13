import json

data = json.load(open("data.json"))

def translate (word):
    word = word.lower()
    if(word in data):
        return data[word]
    else:
        return "Word not found"

word = input("Enter a word: ")

print(translate(word))