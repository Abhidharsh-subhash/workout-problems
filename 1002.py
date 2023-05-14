#incomplete

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

def repeating(array):
    result=[]
    for i in array:
        for j in i:
            if (j in array[1]) and (j in array[2]):
                if j not in result:
                    result.append(j) 
        break
    return result

words = ["cool","lock","cook"]
print(repeating(words))