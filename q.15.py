import math

a = int(input("Enter the number of students in class 1: "))
b = int(input("Enter the number of students in class 2: "))
c = int(input("Enter the number of students in class 3: "))

desks_a = math.ceil(a / 2)  
desks_b = math.ceil(b / 2)
desks_c = math.ceil(c / 2)

total_desks = desks_a + desks_b + desks_c

print(f"The total number of desks required is: {total_desks}")