list1 = []
list2 = []

num = input("enter an integer: ENTER to exit ")
while num != "":
    list1.append(int(num))
    num = input("enter an integer: ENTER to exit ")

num = input("enter an integer: ENTER to exit ")
while num != "":
    list2.append(int(num))
    num = input("enter an integer: ENTER to exit ")

if len(list1) == len(list2):
    print("lists are the same length")

if sum(list1) == sum(list2):
    print("lists sum to the dame total")

for i in range(len(list1)):
    if list1[i] in list2:
        print("there is a identical value in both lists")
        break
