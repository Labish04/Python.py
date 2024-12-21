subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))

# Calculate total marks and percentage
total_marks = subject1 + subject2 + subject3 + subject4
percentage = (total_marks / 400) * 100  # Assuming each subject has a maximum of 100 marks

# Display total marks and percentage
print("\nTotal Marks: ", total_marks)
print("Percentage: ", percentage)

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Grade: ", grade)