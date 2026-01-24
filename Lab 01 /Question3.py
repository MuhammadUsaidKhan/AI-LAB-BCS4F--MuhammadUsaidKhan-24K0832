dict = {}
count = 0
while (count<3):
    name = input("Enter Student name: ")
    marks = int(input("Enter Marks: "))
    dict[name] = marks
    count = count + 1
    
print("Student Records: ")
print(dict)
