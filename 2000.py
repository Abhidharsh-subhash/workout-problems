# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

def reversePrefix(word,ch):
    index=0
    for i in range(len(word)):
        if word[i] == ch:
            index=i
            break
    x=word[:index+1]
    a=x[::-1]
    y=word[index+1::]
    result=a+y
    return result

word = "abcd"
ch = "z"
print(reversePrefix(word,ch))

