lst = [10,9,8,7,6,5,4,3,2,1,0]

lenlst = len(lst)
largest = 0
for i in range(lenlst//2, lenlst):
    if lst[i] > largest:
        largest = lst[i]

print(largest)