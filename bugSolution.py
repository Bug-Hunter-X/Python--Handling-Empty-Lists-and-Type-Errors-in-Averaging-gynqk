def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle the case where no numeric values are present
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: 0

my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: 20.0

my_numbers = [10, 20, 'a']
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: 15.0

my_numbers = ['a', 'b', 'c']
average = calculate_average(my_numbers)
print(f"The average is: {average}") # Output: 0