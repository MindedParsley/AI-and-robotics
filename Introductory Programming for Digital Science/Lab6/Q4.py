#count how many e's are in the file

with open("Lab6/texts/deepseek.txt", "r") as txt:
    text = txt.read()
    print(f"the total amount of e in the file was {text.lower().count("e")}")


