# Input: s = "()"
# Output: true

def isValid(s):
    # while '()' in s or '[]'in s or '{}' in s:
    #     s = s.replace('()','').replace('[]','').replace('{}','')
    # return False if len(s) !=0 else True
    for i in range(len(s)):
        if ('()' in s) or ('[]' in s) or ('{}' in s):
            s=s.replace('()','').replace('[]','').replace('{}','')
        if len(s) == 0:
            return True
    return False

s = "(]"
print(isValid(s))