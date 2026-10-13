#Q13

num = int(input("enter a number: "))
result = ""

if num%3 == 0:
    result = result + "Fizz"

if num%5 == 0:
    result = result + "buzz"

print(f"result: {result}")