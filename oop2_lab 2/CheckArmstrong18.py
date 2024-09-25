# R ektu bujhte hobe
def is_Armstrong(number):
    power = len(str(number))
    total = sum(int(digit) ** power for digit in str(number))
    return total == number


number = 100
print(f"{number} is Armstrong number:{is_Armstrong(number)}")