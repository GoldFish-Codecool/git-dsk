# **Text Analyzer**:
# - Create a program that reads a text file and provides statistics like word count, sentence count, most common words, and average word length.

# Dana
def enter_text():
    text = input("Enter text: ")
    file_name = "Tamas_text_analyzer.txt"
    with open(file_name, "w") as file:
      file.write(text)

# Dorothy
def word_count():
    with open("Tamas_text_analyzer.txt", "r") as file:
      content = file.read()
      words = content.split()
    return len(words)

# Petko
def sentence_count():
    with open("Tamas_text_analyzer.txt", "r") as file:
      content = file.read()
      sentences = content.split(".")
    return len(sentences)

# Mihail
def average_wordlength():
  with open("Tamas_text_analyzer.txt", "r") as file:
    content = file.read()
    words = content.split()
    average = 0
    for i in range(len(words)):
      average = average + len(words[i])
    length = average / len(words)  
    formatted_length = "{:.2f}".format(length)
  return formatted_length

# Boyan
def most_common_word():
  with open("Tamas_text_analyzer.txt", "r") as file:
    content = file.read()
    words = content.split()
    
    
    max_count = 0
    
    for i in range(len(words)):
      count = 0
      for j in range(len(words)):
        if words[i] == words[j]:
          count = count + 1

      if count > max_count :
        max_count = count
        max_word = words[i]

  return (max_word, max_count)
  
# Gabor
def menu():
  print("1. Count sentences")
  print("2. Count words")
  print("3. Average word length")
  print("4. Most common word")
  print("5. Quit")
  choice = int(input("What is your choice\n\n"))
  return choice

# Tamas
if __name__=="__main__":
  enter_text()
  
  choice = menu()

  while choice != 5:
  
    if choice == 1:
      print(f"\nnThere are {sentence_count()} sentences in the text.\n\n")
    
    elif choice == 2:
      print(f"\n\nThere are {word_count()} words in the text\n\n")

    elif choice == 3:
      print(f"\n\nThe average word length is {average_wordlength()}\n\n")

    elif choice == 4:
      print(f"\n\n The most frequent word is {most_common_word()}.\n\n")

    choice = menu()



   
  
  



