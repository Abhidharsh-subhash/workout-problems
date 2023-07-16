# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

def isPrefixOfWord(sentence,searchWord):
    if searchWord in sentence:
        result=1
        length=len(searchWord)
        i=0
        while i<len(sentence):
            if result == 1:
                x=sentence[:length]
                if x == searchWord:
                    return result
            elif sentence[i] == ' ':
                result+=1
                x=sentence[(i+1):(i+1+length)]
                if x == searchWord:
                    return result
            i+=1
    else:
        return -1

sentence = "leetcode corona"
searchWord = "leetco"
print(isPrefixOfWord(sentence,searchWord))

