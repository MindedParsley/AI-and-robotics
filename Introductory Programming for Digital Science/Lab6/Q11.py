date = input("enter a date: ")
replacement = input("enter the replacement character: ")

for i in range(len(date)):
    if not date[i].isnumeric():
        newdate = date.replace(date[i], replacement)
        print(newdate)
        break