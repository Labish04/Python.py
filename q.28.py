score = float(input("Enter your subject score: "))

if score > 90:
    print("Congratulations! You did an excellent job!")
elif 50 <= score <= 90:
    print("Good job! But there's room for improvement.")
else:
    print("You need to retake the course. Keep working hard!")