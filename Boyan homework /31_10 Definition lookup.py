from PyDictionary import PyDictionary

dictionary = PyDictionary()

word = input("Enter a word: ")

definition = dictionary.meaning(word)
print(definition)

synonyms = dictionary.synonym(word)
print(synonyms)
