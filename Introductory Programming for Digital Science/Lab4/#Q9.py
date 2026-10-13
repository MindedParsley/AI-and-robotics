#Q9

month = input("enter a month: ")
letter = input("enter a letter to find: ")
found = False

for i in range(len(month)):
    if month[i].lower() == letter.lower():
        found = True
        break

print(found)
