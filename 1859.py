# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

def sortSentence(s):
    result=''
    count=1
    i=0
    index=0
    while i<len(s):
        if s[i] == str(count):
            count+=1
            i=0
            for j in range(i-1,-1,-1):
                if s[j] == ' ':
                    break
                else:
                    index=j
            print(s[index+1:i-1])
        else:
            i+=1

s = "is2 sentence4 This1 a3"
sortSentence(s)