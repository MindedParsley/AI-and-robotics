name = input("enter a name: press ENTER to exit: ")
a = 0
while name != "":
    for i in range(len(name)):
        if name[i].lower() == "a":
            a += 1
    name = input("enter a name: press ENTER to exit: ")
print(f"the amount of a: {a}")