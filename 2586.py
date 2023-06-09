# Input: words = ["are","amy","u"], left = 0, right = 2
# Output: 2
# Explanation: 
# - "are" is a vowel string because it starts with 'a' and ends with 'e'.
# - "amy" is not a vowel string because it does not end with a vowel.
# - "u" is a vowel string because it starts with 'u' and ends with 'u'.
# The number of vowel strings in the mentioned range is 2.
# Example 2:

# Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
# Output: 3
# Explanation: 
# - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
# - "mu" is not a vowel string because it does not start with a vowel.
# - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
# - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
# The number of vowel strings in the mentioned range is 3.

def vowelstrings(words,left,right):
    vowels=['a', 'e', 'i', 'o','u']
    count=0
    for i in range(left,right+1):
        word=words[i]
        if (word[0] in vowels) and (word[-1] in vowels):
            count+=1
    return count

words=["are","amy","u"]
print(vowelstrings(words,0,2))
