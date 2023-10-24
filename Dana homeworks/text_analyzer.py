#Text Analyzer: Create a program that reads a text file and provides statistics like word count, sentence count, most common words, and average word length.

import collections
import re

filename = input("Enter the name of the file: ")

with open(filename, "r") as file:
    reading = file.read()
    print(f"\nThe text of the file is as follows: \n\"{reading}\"")

    words = reading.split()
    word_count = len(words)
    sentences = len(re.findall(r'[.!?]', reading))
    print(f"\nThe file contains {word_count} words in {sentences} sentence(s).")

total_word_length = sum(len(word) for word in words)
average_word_length = total_word_length / word_count
print(f"The average length of words is {average_word_length:.2f} characters.")

word_counts = collections.Counter(words)
most_common_words = word_counts.most_common()

max_occurrence = most_common_words[0][1]
print("The most common word(s) is/are:")
for word, count in most_common_words:
  if count == max_occurrence:
    print(f"'{word}' with {count} occurrences.")
  else:
    break
