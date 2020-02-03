"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.profit = []
        self.helper(0, 0, 0)
        return max(self.profit)
        
    # have 0:未持有  1:持有
    def helper(self, i, have, profit):
        if i == len(self.prices):
            self.profit.append(profit)
            return
        if have: # 如果持有中
            self.helper(i+1, 0, profit + self.prices[i]) # 卖出
            self.helper(i+1, 1, profit) # 不动
        else: # 如果未持有
            self.helper(i+1, 0, profit) # 不动
            self.helper(i+1, 1, profit - self.prices[i]) # 买入
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp> 0:
                profit += tmp
        return profit

