#Q8

product = 1
num = input("enter a num: ")
while num != "0":
    product *= int(num)
    num = input("enter a num: ")

print(f"product: {product}")