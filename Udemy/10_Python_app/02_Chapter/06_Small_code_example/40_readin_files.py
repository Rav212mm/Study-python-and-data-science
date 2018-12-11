# Open a file
readed = open("fruits.txt")
content = readed.read()
readed.close()
print('\n', content.splitlines(), '\n')