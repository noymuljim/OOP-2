#quadratic equation = ax*x + bx + c=0
# x= -b+- root b**2-4ac/2a

import math


def solve_quadratic(a, b, c):
    
    dis = b**2 - 4*a*c
    
    if dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
        return root1, root2
    
    elif dis == 0:
        
        root = -b / (2 * a)
        return root
    else:
        
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-dis) / (2 * a)
        return (real_part, imaginary_part)
    

a = float(input("Enter  a: "))
b = float(input("Enter  b: "))
c = float(input("Enter  c: "))

solution = solve_quadratic(a, b, c)

if isinstance(solution, tuple):
    if len(solution) == 2:
        print(f"The solutions are:" ,solution)
    else:
        print(f"The solution is:",solution)
else:
    print(f"The complex solutions are: ",solution)
