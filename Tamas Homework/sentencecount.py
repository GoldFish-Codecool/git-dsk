# Petko
def sentence_count():
    with open("Tamas_text_analyzer.txt", "r") as file:
      content = file.read()
      sentences = content.split(".")
    return len(sentences)