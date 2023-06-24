# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    # low=float('inf')
    # for i in range(len(prices)):
    #     low=min(low,prices[i])
    #     index=prices.index(low)
    # high=low
    # for i in range(index,len(prices)):
    #     if prices[i] > high:
    #         high=prices[i]
    # if (high == low):
    #     return 0
    # else:
    #     profit=high-low
    #     return profit 
    profit=0
    low=float('inf')
    for i in prices:
        if low > i:
            low=i
        elif i-low > profit:
            profit=i-low
    return profit

prices =[7,6,4,3,1]
print(maxProfit(prices))