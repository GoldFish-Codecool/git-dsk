#Dictionary and Thesaurus Lookup: Create a program that allows users to enter a word and get its definition and synonyms. (Requires: PyDictionary library or an API like WordNet)

from PyDictionary import PyDictionary

def word_lookup(word):
    dictionary = PyDictionary()  
    definition = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)

    print("Definition(s):")
    if definition and 'Noun' in definition:
        print(", ".join(definition['Noun'])) 

    print("Synonyms:")
    if synonyms:
        print(", ".join(synonyms))
    else:
        print("Synonyms not found.")

if __name__ == "__main__":
    word = input("Enter a word: ")  
    word_lookup(word)  
