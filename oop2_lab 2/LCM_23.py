def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


a = 12
b = 15
print(f"LCM of {a} and {b} is {lcm(a, b)}")