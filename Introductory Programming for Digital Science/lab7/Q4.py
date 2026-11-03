import Calculator as C

def PickNum():
    while True:
        try:
            num1 = int(input("enter a number: "))
            num2 = int(input("enter number 2: "))
            break
        except:
            print("ERROR: enter a valid number")
    return num1,num2

chosenOp = ""
while True:
    chosenOp = input("enter +,-,/,* : press ENTER to exit")
    match chosenOp:
        case "+":
            C.add(*PickNum())
        case "-":
            C.subtract(*PickNum())
        case "*":
            C.multiply(*PickNum())
        case "/":
            C.divide(*PickNum())
        case "":
            break
        case _:
            print("please enter a valid operation")
