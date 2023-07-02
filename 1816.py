# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".

def truncateSentence(s,k):
    n=s.strip()
    count=0
    result=''
    for i in n:
        if i == ' ':
            result+=i
            count+=1
        else:
            result+=i
        if count == k:
            break
    return (result.strip())
        
    

s = "chopper is not a tanuki"
k = 5
print(truncateSentence(s,k))