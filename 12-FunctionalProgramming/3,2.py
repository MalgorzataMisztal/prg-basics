sentence = 'I completely agree with you'
words = sentence.split()
result = list(map(lambda word: len(word), words))

print(sentence)
print(f"No. of letters in words: {result}")