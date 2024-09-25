#Triangle_area = 0.5*B*H

def Triangle_area(base,height):
    area = 0.5 *base*height
    return area

base=float(input("Enter the first triangle:"))
height=float(input("enter the second triangle:"))

area=Triangle_area(base,height)

print(f"The area of the triangle is:",area)