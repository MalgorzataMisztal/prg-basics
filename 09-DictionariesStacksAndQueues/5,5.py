paragraph = "cat dog mouse cat rat cat mouse"
words = paragraph.split()

counter = {}
for i in words:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

for word, count in counter.items():
    print(f'{word}: {count}')