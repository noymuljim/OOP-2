
def km_to_miles(kilometers):
    convesion_fac = 0.621371
    miles= kilometers * convesion_fac
    
    return miles

kilometers=float(input("Enter the distance in kilo:"))

miles = km_to_miles(kilometers)

print(f"{kilometers} kilometers is equal to {miles} miles")