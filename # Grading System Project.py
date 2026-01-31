# Grading System Project

marks = int(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    print("Grade: A+")
elif marks >= 70 and marks <= 79:
    print("Grade: A")
elif marks >= 60 and marks <= 69:
    print("Grade: B")
elif marks >= 50 and marks <= 59:
    print("Grade: C")
elif marks >= 40 and marks <= 49:
    print("Grade: D")
elif marks >= 0 and marks < 40:
    print("Grade: F (Fail)")
else:
    print("Invalid marks! Please enter marks between 0 and 100.")