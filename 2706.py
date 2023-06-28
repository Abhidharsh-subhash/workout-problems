# Input: prices = [1,2,2], money = 3
# Output: 0
# Explanation: Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

def buyChoco(prices,money):
    result=money
    for i in range(len(prices)):
        n=prices[i]
        for j in range(i+1,len(prices)):
            if n+prices[j]<=money and result<money-(n+prices[j]):
                result=money-(n+prices[j])
    return result

prices=[98,54,6,34,66,63,52,39]
print(buyChoco(prices,62))

