def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    total = sum(numbers)
    average = total / len(numbers) 
    return average

my_numbers = []
average = calculate_average(my_numbers) 
print(f"The average is: {average}") #This will return 0 because of the empty list

my_numbers = [10, 20, 30]
average = calculate_average(my_numbers) 
print(f"The average is: {average}") #This will return the average

my_numbers = [10, 20, 'a']
average = calculate_average(my_numbers) 
print(f"The average is: {average}")  # This will throw TypeError