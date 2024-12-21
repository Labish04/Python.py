age = int(input("Enter the candidate's age: "))

if age >= 18:
    has_degree = input("Do you have a degree? (yes/no): ")
    if has_degree == "yes":
        experience = float(input("Enter your work experience in years: "))
        if experience > 3:
            print("Highly Eligible.")
        elif 1 <= experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Not Eligible. A degree is required.")
else:
    print("Not Eligible. Age must be 18 or above.")