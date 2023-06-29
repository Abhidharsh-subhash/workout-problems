# Input: words = ["cd","ac","dc","ca","zz"]
# Output: 2
# Explanation: In this example, we can form 2 pair of strings in the following way:
# - We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
# - We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
# It can be proven that 2 is the maximum number of pairs that can be formed.

def maximumNumberOfStringPairs(words):
    count=0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            x=words[j]
            if words[i] == x[::-1]:
                count+=1
                break
    return count

words=["aa","ab"]
print(maximumNumberOfStringPairs(words))