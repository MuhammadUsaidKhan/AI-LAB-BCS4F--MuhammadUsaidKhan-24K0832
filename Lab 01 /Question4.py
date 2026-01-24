print("1. Add two Numbers")
print("2. Subtract two Numbers")
print("3. Exit")
choice = int(input("Enter Your Choice: "))
while (choice != 3):
    if choice == 1:
        first_number = int(input("Enter First Number: "))
        second_number = int(input("Enter Second Number: "))
        result = first_number + second_number
        print("Result: ", result)
        print("1. Add two Numbers")
        print("2. Subtract two Numbers")
        print("3. Exit")
        choice = int(input("Enter your Choice: "))
    elif choice == 2:
        first_number = int(input("Enter First Number: "))
        second_number = int(input("Enter Second Number: "))
        result = first_number - second_number
        print("Result: ", result)
        print("1. Add two Numbers")
        print("2. Subtract two Numbers")
        print("3. Exit")
        choice = int(input("Enter your Choice: "))
    else:
        print("1. Add two Numbers")
        print("2. Subtract two Numbers")
        print("3. Exit")
        choice = int(input("Enter your Choice: "))
