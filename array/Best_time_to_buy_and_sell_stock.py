"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Not 7-1 = 6, as selling price needs to be larger than buying price.

"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        L = 0
        min_prices = prices[0]
        max_profit = 0
        while(L < len(prices)-1):
            L = L+1
            if(min_prices>prices[L]):
                min_prices = prices[L]
            if(max_profit < prices[L] -min_prices):
                max_profit = prices[L] -min_prices

        return max_profit
