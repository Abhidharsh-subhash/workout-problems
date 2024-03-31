# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

def wordPattern(pattern: str, s: str):
    x=list(pattern)
    y=s.split(' ')
    if len(x) != len(y):
        return False
    z={}
    for i in range(len(x)):
        if (x[i] not in z.keys()) and (y[i] not in z.values()):
            z[x[i]]=y[i]
        elif z.get(x[i]) is None:
            return False
        elif z[x[i]] != y[i]:
            return False
    return True

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern,s))