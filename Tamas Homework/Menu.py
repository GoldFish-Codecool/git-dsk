def word_count():
    with open("Tamas_text_analyzer.txt", "r") as file:
      content = file.read()
      words = content.split()
    return len(words)
