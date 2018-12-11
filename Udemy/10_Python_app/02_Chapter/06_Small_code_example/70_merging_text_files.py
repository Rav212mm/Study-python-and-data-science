import glob2
from datetime import datetime

file_list = glob2.glob('*/*.txt')
file_list

print(file_list)

new_name =datetime.now()
print(type(new_name))
print(new_name)

text_name = new_name.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(type(text_name))
print(text_name)

with open(text_name, 'w') as myfile:
    for i in file_list:
        opened = open(i, 'r')
        readed = opened.read()
        print(readed)
        myfile.write(readed + '\n')
        opened.close()

with open(text_name, 'r') as myfile:
    print('Zawartość nowego pliku: ' + '\n'+ myfile.read())
