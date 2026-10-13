#Q10

start = int(input("enter a number to start counting on: "))
end = int(input("enter a number to finish counting on: "))
total =0
for i in range(start,end+1):
    if (i%2) == 0:
        total += i

print(total)