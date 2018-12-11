def open_file(name):
    opened = open(name)
    content = opened.read()
    opened.seek()
    opened.close()

    print(content)

file_name = 'sample.txt'

open_file(file_name)