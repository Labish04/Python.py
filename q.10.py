grade = float(input("Enter the grade: "))

if grade < 25:
    print("Grade: D")
elif 25 <= grade < 45:
    print("Grade: C")
elif 45 <= grade < 50:
    print("Grade: B")
elif 50 <= grade < 60:
    print("Grade: B+")
elif 60 <= grade < 80:
    print("Grade: A")
else:  # Above 80
    print("Grade: A+")