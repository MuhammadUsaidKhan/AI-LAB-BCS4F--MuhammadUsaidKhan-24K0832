class StudentResult:
  def __init__(self, name, roll_number, marks):
    self.name = name
    self.roll_number = roll_number
    self.__marks = marks

  def display_details(self):
    print(f"Name: {self.name}")
    print(f"Roll Number: {self.roll_number}")
    print(f"Marks: {self.__marks}")
        
  def set_marks(self, marks):
    if 0 <= marks <= 100:
      self.__marks = marks

  def get_marks(self):
    return self.__marks

  def calculate_grade(self):
    marks = self.get_marks()
    if marks >=90:
      return "A+"
    elif marks >=80:
      return "A"
    elif marks >=70:
      return "B"
    elif marks >=60:
      return "C"
    elif marks >=50:
      return "D"
    else:
      return "F"

student1 = StudentResult("Usaid", "0832", 85)
student1.display_details()
student1.set_marks(92)
student1.display_details()
print(f"Grade: {student1.calculate_grade()}")

student2 = StudentResult("Sufi", "0190", 78)
student2.display_details()
student2.set_marks(60)
student2.display_details()
print(f"Grade: {student2.calculate_grade()}")
