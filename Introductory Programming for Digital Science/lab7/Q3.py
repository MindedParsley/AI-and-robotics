def Func_a():
    print(4/0)

def Func_b():
    try:
        Func_a()
    except ZeroDivisionError:
        print("ZeroDivisionError - change the divide")
        Func_a()

def Func_c():
    try: 
        Func_b()
    except:
        print("Please disperse, there is nothing to see here…") 


Func_c()