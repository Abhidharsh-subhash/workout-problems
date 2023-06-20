# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

def maximumWealth(accounts):
    result=0
    for i in range(len(accounts)):
        sum=0
        for j in range(len(accounts[i])):
            sum+=accounts[i][j]
        if result<sum:
            result=sum
    return result

accounts = [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))