def revstring(string):
    words = string.split()  # Split the string into individual words
    result = []
    
    for word in words:
        result.append(word[::-1])  # Reverse each word and add it to the result list
        print(result)
    
    return ' '.join(result)  # Join the reversed words with spaces

string = 'my name is abhidharsh'
print(revstring(string))