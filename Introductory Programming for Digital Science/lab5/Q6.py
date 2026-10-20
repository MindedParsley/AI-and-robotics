number = input("enter a number: (1-100) press ENTER to exit: ")
listNum = []
while number != "":
    try:
        if (int(number) > 0 and int(number) <= 100):
            listNum.append(int(number))
    except:
        pass
    number = input("enter a number: (1-100) press ENTER to exit: ")

print(listNum)