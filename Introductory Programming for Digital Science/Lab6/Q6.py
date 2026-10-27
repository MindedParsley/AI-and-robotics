string = "This  line  has   extra    space    characters"
splitString = string.split(" ")
wordOnly = [i for i in splitString if i != '']

output = ""
for i in range(len(wordOnly)):
    output += f"{wordOnly[i]} "

print(output)