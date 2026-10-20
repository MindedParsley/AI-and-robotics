list1 = [1,2,3,4,5,6]
odds = []
for num in range(len(list1)):
    if num%2 == 1:
        odds.append(num)
print(odds)