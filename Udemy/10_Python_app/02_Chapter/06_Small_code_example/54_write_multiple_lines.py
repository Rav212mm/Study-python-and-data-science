numbers = [1, 2, 3]
myfile = open('sample_text', 'w')

for item in numbers:
    myfile.write(str(item) + '\n')

myfile.close()