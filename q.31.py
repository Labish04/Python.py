income = float(input("Enter your annual income: "))

if income > 50000:
    credit_score = int(input("Enter your credit score: "))
    if credit_score > 700:
        print("Loan Approved.")
    elif 600 <= credit_score <= 700:
        print("Loan Approved with a higher interest rate.")
    else:
        print("Loan Rejected. Credit score is too low.")
else:
    print("Loan Rejected. Income is below the qualifying threshold.")