num = int(input("enter the number to convert: "))

def binary_i(num):

    if num == 0:
        return "0"

    sign = "-" if num < 0 else ""
    num = abs(num)

    bits = []
    while num > 0:
        bits.append(str(num % 2))
        num //= 2

    return sign + "".join(reversed(bits))


def binary_r(num):
    if num == 0:
        return "0"

    if num < 0:
        return "-" + binary_r(-num)

    if num < 2:
        return str(num)

    return binary_r(num // 2) + str(num % 2)


print(f"recursive: {binary_r(num)}")
print(f"iterative: {binary_i(num)}")