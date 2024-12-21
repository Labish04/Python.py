cost_price = float(input("Enter the cost price of the bike in Rs: "))

if cost_price > 100000:
    tax = (15 / 100) * cost_price  # 15% tax
elif cost_price > 50000 and cost_price <= 100000:
    tax = (10 / 100) * cost_price  # 10% tax
else:
    tax = (5 / 100) * cost_price  # 5% tax

print(f"The road tax to be paid is Rs: {tax}")