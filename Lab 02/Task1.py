class Vehicle:
  def __init__(self, vehicle_id, brand, rent_per_day):
    self.vehicle_id = vehicle_id
    self.brand = brand
    self.rent_per_day = rent_per_day

  def display_details(self):
    print(f"Vehicle ID: {self.vehicle_id}")
    print(f"Brand: {self.brand}")
    print(f"Rent per Day: {self.rent_per_day}")

  def calculate_rent(self, days):
    return self.rent_per_day * days

corolla = Vehicle("ABC123", "Toyota", 50)
corolla.display_details()
rent_days = 3
total_rent = corolla.calculate_rent(rent_days)
print(f"Corolla Total Rent for {rent_days} days: {total_rent}")
rent_days = 5
total_rent = corolla.calculate_rent(rent_days)
print(f"Corolla Total Rent for {rent_days} days: {total_rent}")
rent_days = 15
total_rent = corolla.calculate_rent(rent_days)
print(f"Corolla Total Rent for {rent_days} days: {total_rent}")

H6 = Vehicle("XYZ789", "HAVAL", 45)
H6.display_details()
rent_days = 2
total_rent = H6.calculate_rent(rent_days)
print(f"Haval H6 HEV Total Rent for {rent_days} days: {total_rent}")
rent_days = 4
total_rent = H6.calculate_rent(rent_days)
print(f"Haval H6 HEV Total Rent for {rent_days} days: {total_rent}")
rent_days = 10
total_rent = H6.calculate_rent(rent_days)
print(f"Haval H6 HEV Total Rent for {rent_days} days: {total_rent}")
