import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


# Example usage:
length = 8
print(generate_random_string(length))