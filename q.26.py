a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(f"The greater number is {a}")
elif b > a:
    print(f"The greater number is {b}")
else:
    print("The numbers are equal.")
    
    if a > 0:
        print("The number is positive.")
    elif a < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")