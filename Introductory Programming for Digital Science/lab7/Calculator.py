def add(num1,num2):
    print(f"answer: {num1+num2}")

def subtract(num1,num2):
    print(f"answer: {num1-num2}")

def multiply(num1,num2):
    print(f"answer: {num1*num2}")

def divide(num1,num2):
    try:
        print(f"answer: {num1/num2}")
    except ZeroDivisionError:
        print("ERROR: dividing by zero")