import re

text = input("Enter the text: ")
pattern = r"[aeiouyąęó]"
vowels_found = re.findall(pattern, text, re.IGNORECASE)
counter = len(vowels_found)
print("Number of vowels in your text: ", counter)