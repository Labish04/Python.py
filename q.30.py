weight = float(input("Enter the package weight in kg: "))

if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else: # weight > 20
    cost = 20

urgent = input("Is the delivery urgent? (yes/no): ").strip().lower()
if urgent == "yes":
    cost += 5
    print(f"The total delivery cost is: ${cost}")