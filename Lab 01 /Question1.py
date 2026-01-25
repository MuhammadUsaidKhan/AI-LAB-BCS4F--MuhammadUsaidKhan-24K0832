name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))

if marks >= 85:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"
    
print("Student Name: ", name)
print("Marks: ", marks)
print("Grade: ", grade)
