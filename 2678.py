# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.

def countSeniors(details):
    result=0
    for i in details:
        x=i[11:13]
        if int(x)>60:
            result+=1
    return result

details = ["1313579440F2036","2921522980M5644"]
print(countSeniors(details))