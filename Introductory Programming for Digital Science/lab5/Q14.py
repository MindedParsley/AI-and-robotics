lst = [1,2,3,4,5,6,7,8,9,]

total = 0
for i in range(len(lst)):
    total += lst[i]
print(total)

total = 0
for i in range(len(lst)):
    total = total + lst[i] + i
print(total)

newlst = []
for i in range(len(lst)):
    newlst.append(lst[len(lst)-i-1])
