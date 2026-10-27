with open("Lab6/texts/numExpressions.txt", "r") as expressions:
    lines = expressions.readlines()
    for i in range(len(lines)):
        num1 = ""
        num2 = ""
        lastNum = 0
        if len(lines[i]) == 0:
            break

        for j in range(len(lines[i])):
            if lines[i][j].isalnum():
                num1 += lines[i][j]
                lastNum = j
            else:
                break

        for j in range(len(lines[i])-4):
            j = j + lastNum +4
            if lines[i][j].isalnum():
                num2 += lines[i][j]
            else:
                break

        match lines[i][lastNum+2]:
            case "+":
                print(f"{num1} + {num2} = {int(num1) + int(num2)}")
            case "-":
                print(f"{num1} - {num2} = {int(num1) - int(num2)}")
            case "/":
                print(f"{num1} / {num2} = {int(num1) / int(num2)}")
            case "*":
                print(f"{num1} * {num2} = {int(num1) * int(num2)}")