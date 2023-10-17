def w (word):
    word = word.replace(" ", "")
    return word == word [::-1]

wd = input ("enter a word: ")
if w (wd):
  print (wd, "is a palindrome")
else:
  print (wd, "is not a palindrome")
