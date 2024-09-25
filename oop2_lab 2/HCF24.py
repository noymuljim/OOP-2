def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


a = 12
b = 15
print(f"HCF of {a} and {b} is {hcf(a, b)}")