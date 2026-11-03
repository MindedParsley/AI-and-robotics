#a
num1 = int(input("enter a number: "))
num2 = int(input("enter a second number: "))

try:
    print(f"{num1} / {num2} = {num1/num2}")
except ZeroDivisionError:
    print("ZeroDivisionError - cant divide by zero")

#b
while True:
    try:
        num1 = int(input("enter a number: "))
        num2 = int(input("enter a second number: "))
        break
    except:
        print("ValueError - input has to be a number")

try:
    print(f"{num1} / {num2} = {num1/num2}")
except ZeroDivisionError:
    print("ZeroDivisionError - cant divide by zero")