days = int(input("Enter the number of days: "))

if days <= 5:
    charge = days * 2  
elif 6 <= days <= 10:
    charge = days * 3  
elif 11 <= days <= 15:
    charge = days * 4  
else:
    charge = days * 5  
    print(f"The total charge for {days} days is: Rs {charge}")