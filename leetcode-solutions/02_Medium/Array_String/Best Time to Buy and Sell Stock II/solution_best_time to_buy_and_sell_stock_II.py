class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        profit = 0
        sum_profit = 0 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                sum_profit += profit
                l += 1
                r += 1
            else:
                l = r
                r += 1
        return sum_profit