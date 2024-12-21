years_of_service = float(input("Enter your years of service:"))
salary = float(input("Enter your salary:"))

if years_of_service > 5:
    bonus = salary * 0.05  
else:
    bonus = 0  
    print(f"The net bonus amount is: Rs {bonus:.2f}")