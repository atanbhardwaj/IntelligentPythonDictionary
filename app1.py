import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? If Yes press Y or If NO press N : " %
                   get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please Double Check it. "
        else:
            return "We didnt understand your entry. "
    else:
        return "The word doesn't exist. Please Double Check it. "


word = input('Enter a word ')

output = translate(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
