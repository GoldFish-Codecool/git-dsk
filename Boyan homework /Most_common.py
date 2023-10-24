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
  