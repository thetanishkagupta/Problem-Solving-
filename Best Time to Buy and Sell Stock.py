class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        max_profit = 0 
        min_so_far = prices[0]
        for i in range(len(prices)):
            min_so_far = min(min_so_far , prices[i])
            profit = prices[i] - min_so_far
            max_profit = max(max_profit , profit)
        return max_profit    
