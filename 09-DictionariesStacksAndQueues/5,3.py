translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input('Enter the word which you want to translate: ').lower()

if word in translations:
    print(f"Translation: {translations[word]}")
else:
    print("Translation is unavailable.")