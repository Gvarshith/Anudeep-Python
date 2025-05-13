def wordscount(filename):
   with open(filename,'r') as file:
      content = file.read()
      words = content.split()
      print("Number of words in the file:", len(words))
wordscount('ABC.txt')