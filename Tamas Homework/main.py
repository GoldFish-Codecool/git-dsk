import menu
import word_count
import sentencecount
import enter_text



# Tamas
if __name__=="__main__":
  enter_text()
  
  choice = menu()

  while choice != 5:
  
    if choice == 1:
      print(f"\nnThere are {sentence_count()} sentences in the text.\n\n")
    
    elif choice == 2:
      print(f"\n\nThere are {word_count()} words in the text\n\n")

#    elif choice == 3:
#      print(f"\n\nThe average word length is {average_wordlength()}\n\n")

#    elif choice == 4:
#      print(f"\n\n The most frequent word is {most_common_word()}.\n\n")

    choice = menu()
