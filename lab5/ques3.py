# Take 5 numbers as input from the user
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display the numbers
print("The numbers are:", numbers)

# Find the maximum without using max()
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Find the minimum without using min()
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

# Display the results
print("Maximum number is:", maximum)
print("Minimum number is:", minimum)
