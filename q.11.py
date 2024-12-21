def calculate_bonus(years_of_service, salary):
    if years_of_service > 10:
        bonus = salary * 0.10
    elif 6 <= years_of_service <= 10:
        bonus = salary * 0.08
    else:
        bonus = salary * 0.05
    return bonus

years_of_service = int(input("Enter years of service: "))
salary = float(input("Enter salary: "))

bonus = calculate_bonus(years_of_service, salary)
print(f"The bonus is: {bonus}")