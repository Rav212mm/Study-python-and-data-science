myfile = open('something.txt', 'w')
myfile.write("Something")
myfile.close()

with open('example.txt', 'w') as myfile:
    myfile.write('Something new')