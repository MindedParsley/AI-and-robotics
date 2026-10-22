#input the starting unsorted string
startList = input("enter the unsorted list: ")
outputList = []

#put the string into a list with no commas or spaces
currentWord = ""
for i in range(len(startList)):
    if startList[i] == "," and currentWord != "":
        print("1")
        outputList.append(currentWord)
        currentWord = ""
    elif startList[i] != " ":
        currentWord = currentWord + startList[i]
outputList.append(currentWord)

#sort list of words
outputList.sort()

#outputing sorted string
outputString = ""
for i in range(len(outputList)):
    if i != len(outputList)-1:
        outputString = outputString + f"{outputList[i]}, "
    else:
        outputString = outputString + outputList[i]

print(outputString)