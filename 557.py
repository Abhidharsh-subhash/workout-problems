# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

def reverseWords(s):
    s=s.strip()
    result=''
    count=0
    for i in range(len(s)):
        if s[i] == ' ' and count == 0:
            count=i
            x=s[:i+1]
            y=x[::-1]
            result+=y
        elif s[i] == ' ':
            x=s[count:i+1]
            y=x[::-1]
            result+=y
            count=i
    x=s[count:len(s)]
    y=x[::-1]
    result+=y
    result=result.strip()
    return result

# return " ".join([x[::-1] for x in s.split()])  here is the single line solution.

s="Let's take LeetCode contest"
print(reverseWords(s))