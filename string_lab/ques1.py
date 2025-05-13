string = " To change the overall look of your document. To change the look available in the gallery "
words = string.split()
# To count the number of occurrences of each word in the string
word_occurrences = {}
for word in words:
    word_occurrences[word] = string.count(word)
print("Word occurrences:", word_occurrences)