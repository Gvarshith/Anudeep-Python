def wordscount(filename):
   uppercase = 0
   with open(filename,'r') as file:
      content = file.read()
      for char in content:
         if char.isupper():
            uppercase += 1
   print(f"Number of uppercase letters in the file: {uppercase}")
wordscount('ABC.txt')