def check_prime(num):
    if num <= 1:
        return f"{num} is not a prime number"
    for i in range(2, int(num**0.5) + 1):
        if num % i==0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"    

num= int(input("Enter a number :"))

print (check_prime(num))