Input = "Hell0 W0rld ! 123 *"

def count_characters(input_string):
    uppercase = lowercase = numbercase = specialCase = 0

    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbercase += 1
        else:
            specialCase += 1

    print(f"Characters in the string are: uppercase = {uppercase}, lowercase = {lowercase}, numbercase = {numbercase}, specialCase = {specialCase}")

count_characters(Input)
