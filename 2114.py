# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation: 
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

from numpy import trim_zeros


def mostWordsFound(sentences):
    result=0
    for i in sentences:
        count=1
        k=i.strip()
        for j in k:
            if j == ' ':
                count+=1
        if result<count:
            result=count
    return result
        
sentences =["please wait", "continue to fight", "continue to win"]
print(mostWordsFound(sentences))

