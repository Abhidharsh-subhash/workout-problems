# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

def checkIfPangram(sentence):
    x={}
    for i in sentence:
        count=0
        for j in range(len(sentence)):
            if sentence[j] == i:
                count+=1
        x.update({i:count})
    n=x.keys()
    if len(n) == 26:
        return True
    else:
        return False
sentence = "leetcode"
print(checkIfPangram(sentence))