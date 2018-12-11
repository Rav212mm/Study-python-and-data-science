import json

word = input('What You are searching for?\nPlease write a word: \n')
print(word)

json_data = open('data.json').read()
type(json_data)

searched_mean = json.loads(json_data)
type(searched_mean)
print(searched_mean[word])