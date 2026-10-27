# return the amount of lines in a file

with open("Lab6/texts/deepseek.txt", "r") as txt:
    lines = txt.readlines()

print(f"the file had {len(lines)} lines")

