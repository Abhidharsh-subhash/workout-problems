# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

def secondHighest(s):
    x=[]
    for i in s:
        if i.isdigit():
            x.append(int(i))
    large=max(x[0],x[1])
    secondlarge=min(x[0],x[1])
    for i in range(2,len(x)):
        if x[i] > large:
            secondlarge=large
            large=x[i]
        elif secondlarge < x[i]:
            secondlarge=x[i]
    if large == secondlarge:
        return -1
    else:
        return secondlarge



s = "abc1111"
print(secondHighest(s))