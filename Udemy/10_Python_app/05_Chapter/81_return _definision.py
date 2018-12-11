import json

def szukaj():
    word = input('\nFind definision :\n')
    opened_dict = json.load(open('data.json'))    
    if word in opened_dict.keys():
        print(opened_dict[word])
    else:
        print('\nNo definition in dictionary.\nSearch a new definition')
        szukaj()

szukaj()