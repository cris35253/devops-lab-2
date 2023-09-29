# average_calculator.py

def compute_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [float(num) for num in input("Enter numbers separated by spaces: ").split()]
average = compute_average(numbers)
print(f"The average of the entered numbers is: {average}")
