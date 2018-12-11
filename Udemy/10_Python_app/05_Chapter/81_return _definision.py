import json

def szukaj(word):
    print('\nDefinision of ',word,':\n')
    word = str(word)                           
    searched_mean = json.load(open('data.json'))
    for i in range(len(searched_mean[word])):
        print(i,')', searched_mean[word][i])

słowo = input('\nSearch in dictionary :')
szukaj(słowo)