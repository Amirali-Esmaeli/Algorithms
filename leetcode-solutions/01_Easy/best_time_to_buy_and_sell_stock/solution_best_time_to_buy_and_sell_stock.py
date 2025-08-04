# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy

# Input: prices = [7,1,5,3,6,4]
# Output: 5


# Solution – Two Pointer O(n)


class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit
