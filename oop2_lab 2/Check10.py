def Check_Number(a):
    if a > 0:
        print("Number is Positive")
    elif a < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")

# Input the number from the user
a = float(input("Enter The Number: "))

# Call the function with the user input
Check_Number(a)