class Employee:
  def __init__(self, name, emp_id):
    self.name = name
    self.emp_id = emp_id

  def display_details(self):
    print(f"Name: {self.name}")
    print(f"Employee ID: {self.emp_id}")

class FullTimeEmployee(Employee):
  def __init__(self, name, emp_id, monthly_salary):
    super().__init__(name, emp_id)
    self.monthly_salary = monthly_salary

  def display_details(self):
    super().display_details()
    print(f"Monthly Salary: {self.monthly_salary}")

  def calculate_salary(self):
    return self.monthly_salary

class PartTimeEmployee(Employee):
  def __init__(self, name, emp_id, hours_worked, hourly_rate):
    super().__init__(name, emp_id)
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate

  def display_details(self):
    super().display_details()
    print(f"Hours Worked: {self.hours_worked}")
    print(f"Hourly Rate: {self.hourly_rate}")

  def calculate_salary(self):
    return self.hours_worked * self.hourly_rate


print("Full-Time Employee Details:")
e1 = FullTimeEmployee("Usaid", "12345", 5000)
e1.display_details()
print(f"Calculated Salary: {e1.calculate_salary()}\n")

print("Part-Time Employee Details:")
e2 = PartTimeEmployee("Sufi", "67890", 40, 15)
e2.display_details()
print(f"Calculated Salary: {e2.calculate_salary()}")
