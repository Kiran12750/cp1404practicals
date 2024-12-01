# Task 1: Ask the user for their name and write it to name.txt
name = input("Please enter your name: ")
file_name = 'name.txt'

# Open name.txt in write mode and save the name
with open(file_name, 'w') as file:
    file.write(name)

# Task 2: Read the name from name.txt and print a greeting
with open(file_name, 'r') as file:
    greeting_name = file.readline().strip()  # Read the name and remove any extra whitespace

# Print the greeting using the name from the file
print(f"Hi {greeting_name}!")

# Task 3: Create numbers.txt and read the first two numbers to print their sum
numbers_file_name = 'numbers.txt'

# Create the file and write the numbers
with open(numbers_file_name, 'w') as numbers_file:
    numbers_file.write("17\n42\n400\n")

# Read the first two numbers and calculate their sum
with open(numbers_file_name, 'r') as numbers_file:
    first_number = int(numbers_file.readline().strip())  # Read the first number
    second_number = int(numbers_file.readline().strip())  # Read the second number
    sum_of_first_two = first_number + second_number

# Print the result of the sum
print(sum_of_first_two)  # Expected output: 59

# Task 4: Calculate and print the total of all numbers in numbers.txt
with open(numbers_file_name, 'r') as numbers_file:
    total_sum = 0
    for line in numbers_file:
        total_sum += int(line.strip())  # Add each number to the total

# Print the total sum of all numbers
print(total_sum)  # This will print the sum of all numbers in the file
