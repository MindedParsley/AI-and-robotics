lst = [1,2,3,4,5]
i = 0
while True:
    try:
        print(lst[i])
        i = i+1
    except IndexError:
        print("list ended - i out of range")
        break

print("done")