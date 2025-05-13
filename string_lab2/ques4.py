input = "Welcome to Python Assignment"
vowels = {'a','e','i','o','u','A','E','I','O','U'}
Vowel_Count = {}
for i in input:
   if i in vowels:
     Vowel_Count[i] = input.count(i)
print("Vowel Count:", Vowel_Count)