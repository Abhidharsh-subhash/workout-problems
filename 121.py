# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    # O(n^2)
    # x=0
    # for i in range(len(prices)-1):
    #     for j in range(i+1,len(prices)):
    #         if prices[j]-prices[i] > x:
    #             x=prices[j]-prices[i]
    # return x
    minprice=prices[0]
    profit=0
    for i in range(1,len(prices)):
        if prices[i] > minprice:
            if prices[i]-minprice > profit:
                profit=prices[i]-minprice
        elif prices[i] < minprice:
            minprice=prices[i]
    return profit

             
prices=[7,1,5,3,6,4]
print(maxProfit(prices))