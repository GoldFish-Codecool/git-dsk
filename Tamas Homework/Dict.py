# 10. **Dictionary and Thesaurus Lookup**:
#  - Create a program that allows users to enter a word and get its definition and synonyms. (Requires: PyDictionary library or an API like WordNet)


from PyDictionary import PyDictionary
dictionary=PyDictionary()

word = input ("Input the word: ")

definition = dictionary.meaning(word)
synonyms = dictionary.synonym(word)
antonyms = dictionary.antonym(word)

print("Definition:", definition)
print("Synonyms:", synonyms) 
print ("Antomys:", antonyms)