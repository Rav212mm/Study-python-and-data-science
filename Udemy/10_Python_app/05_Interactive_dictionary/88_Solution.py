import json
import difflib

def szukaj():
    
    word = input('\nFind definision :\n').lower()
    opened_dict = json.load(open('data.json'))
    similar = difflib.get_close_matches(word, opened_dict.keys(), n=1, cutoff=0.8)
    
    if word in opened_dict:
        for i in opened_dict[word]:
            return print(i)
    
    elif word.title() in opened_dict:
        print('\nYou mean: %s' %word.title())
        for i in opened_dict[word.title()]:
            return print(i)   
    
    elif word.upper() in opened_dict:
        print('\nYou mean: %s' %word.upper())
        for i in opened_dict[word.upper()]:
            return print(i)  
    
    elif len(similar) == 1:
        odp = input('\nCzy chodziło Ci o :%s? (Y/N)\n' %similar[0])
        if str(odp).upper() == 'Y':
            print('\n%s definision:' %similar[0])
            for i in opened_dict[similar[0]]:
                return print(i)
        
        else:
            print('\nNo definition in dictionary.\nSearch a new definition')
            szukaj()
   
    else:
        print('\nNo definition in dictionary.\nSearch a new definition')
        szukaj()

szukaj()