# lists_warmup.py

# Initialize the list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Expected values for the expressions:
# numbers[0] => 3
# numbers[-1] => 2
# numbers[3] => 1
# numbers[:-1] => [3, 1, 4, 1, 5, 9]
# numbers[3:4] => [1]
# 5 in numbers => True
# 7 in numbers => False
# "3" in numbers => False
# numbers + [6, 5, 3] => [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modify the list
numbers[0] = "ten"  # Change the first element to the string "ten"
numbers[-1] = 1     # Change the last element to 1

# Print elements from numbers except the first two
print(numbers[2:])

# Check if 9 is an element of numbers
print(9 in numbers)
