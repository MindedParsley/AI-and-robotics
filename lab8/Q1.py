d1 = {1:10,2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}

#a
d4 = {**d1, **d2, **d3}
print(d4)

#b
d4[7] = 70
print(d4)

#c
d4[3] = 80
print(d4)

#d
i = 3
d4.pop(list(d4.keys())[i-1])
print(d4)

#e
sumValue = sum(list(d4.values()))
print(sumValue)

#f
print(min(d4, key=d4.get))

#g
print(max(d4, key=d4.get))