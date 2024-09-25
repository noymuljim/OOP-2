def all_prime(n):
    if n <= 1: 
     # ≤ 1 is not prime then return false
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def print_prime_interval(start, end):
    for num in range(start, end + 1):
        if all_prime(num):
            print(num)


start = 10
end = 100
print_prime_interval(start, end)