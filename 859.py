# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

def buddyStrings(s,goal):
    for i in range(len(s)):
        if s[i] == goal[i]:
            pass
        else:
            for j in range(i+1,len(s)):
                if s[j] == go

s = "ab"
goal = "ab"
print(buddyStrings(s,goal))