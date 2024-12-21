N = int(input("Enter the number of students (N): "))
K = int(input("Enter the number of apples (K): "))

apples_per_student = K // N
apples_remaining = K % N

print("Each student gets:", apples_per_student)
print("Apples remaining in the basket:", apples_remaining)