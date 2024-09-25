# Fn = Fn-1+Fn-2
def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = 10
Fibonacci(n)