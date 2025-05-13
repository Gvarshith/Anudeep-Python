def display_words():
    words = []
    with open("story.txt", "r") as file:
      for line in file:
        words = line.split()
    print("Words with less than 5 characters:")
    for word in words:
        if len(word) < 4:
            print(word ,end=",")
display_words()