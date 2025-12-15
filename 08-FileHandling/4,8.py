import re

with open('files.txt', 'r', encoding = 'utf-8') as file:
    content = file.read()

pattern = r'\w+\.\w{4}\b'

founded = re.findall(pattern, content)
for name in founded:
    print(name)