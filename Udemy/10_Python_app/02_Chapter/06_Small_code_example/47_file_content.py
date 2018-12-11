opened = open('fruits.txt')
content = opened.read()
content_splitlines = content.splitlines()

for item in content_splitlines:
    print(item)
    print(len(item))
opened.close()

print(content.strip()