import nltk

from nltk.corpus import wordnet

nltk.download('wordnet')

def word_lookup(word):
  synonyms = set()
  definitions = []

  for syn in wordnet.synsets(word):
      definitions.append(syn.definition())
      for lemma in syn.lemmas():
          synonyms.add(lemma.name())

  print("Definitions:")
  print("\n".join(definitions) or "Not found.")

  print("\nSynonyms:")
  print(", ".join(synonyms) or "Not found.")

if __name__ == "__main__":
  word = input("Enter a word: ")
  word_lookup(word)
