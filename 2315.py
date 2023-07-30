# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.

def countAsterisks(s):
    count=1
    result=0
    for i in s:
        if i == '|':
            count+=1
        elif (count % 2 == 1) and (i == '*'):
            result+=1
    return result


s = "yo|uar|e**|b|e***au|tifu|l"
print(countAsterisks(s))