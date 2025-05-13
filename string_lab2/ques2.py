input = "String and String Function"

def removeDuplicates(input):
    # Split the string into words
    words = input.split()
    # Create a list to store the result
    result = []
    # Iterate through each word in the input string
    for word in words:
        # If the word is not already in the set, add it to the set and the result list
        if word not in result:
            result.append(word)
    
    # Join the result list into a string and return it
    return ' '.join(result)
 

result = removeDuplicates(input)
print("Input String:", result)