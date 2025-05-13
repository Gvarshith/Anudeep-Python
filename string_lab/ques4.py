String= "Welcome to python Training"
vowels = {'a','e','i','o','u','A','E','I','O','U'}
Vowel_Count = {}
for i in String:
   if i in vowels:
     Vowel_Count[i] = String.count(i)
print("Vowel Count:", Vowel_Count)
     
    