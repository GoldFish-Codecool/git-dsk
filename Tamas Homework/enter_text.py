def enter_text():
    text = input("Enter text: ")
    file_name = "Tamas_text_analyzer.txt"
    with open(file_name, "w") as file:
      file.write(text)