def calculate_average(a, size):
    i = 0
    sum1 = 0
    while (i<size):
        sum1 = sum1 + a[i]
        i = i + 1
        
    average = sum1 / size
    return average
    
list1 = [46, 90, 69, 45, 73, 99]
average = calculate_average(list1, 6)
print("Marks: ", list1)
print("Average Marks: ", average)
