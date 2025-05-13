# Program to count letters, digits, and special symbols in a string

def count_characters(input_string):
  letters = digits = special_symbols = 0

  for char in input_string:
    if char.isalpha():
      letters += 1
    elif char.isdigit():
      digits += 1
    else:
      special_symbols += 1

  return letters, digits, special_symbols

# Input string
input_string = "P@#yn26at^&i5ve"

# Count characters
letters, digits, special_symbols = count_characters(input_string)

# Display results
print("Letters:", letters)
print("Digits:", digits)
print("Special Symbols:", special_symbols)


