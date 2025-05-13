def readfile(filename):
    with open(filename, 'r') as file:
      content = file.read()
      print(content)
readfile('ABC.txt')
