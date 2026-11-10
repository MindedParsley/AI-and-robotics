set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

#a
set3 = set1 | set2
print(set3)

#b
set4 = set1 & set2
print(set4)

#c
set5 = set1 - set2
print(set5)

#d
set2.remove(20)
print(set2)