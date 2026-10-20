string1 = input("enter the string: ")
pos = int(input("enter what character possition you want to find: "))
char = input("enter what charcacter you want to find the position of: ")

if int(pos) <= len(string1):
    print(string1[pos])

for i in range(len(string1)):
    if string1[i].lower() == char.lower():
        print(i)
        break