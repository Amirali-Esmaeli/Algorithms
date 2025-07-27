# Best Time to Buy and Sell Stock

## Problem

You are given an array prices where prices[i] is the price of a given stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Example:**

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

## Solutions

### ✅ Two Pointers 
Use two pointers (left for buy day, right for sell day).
Move the pointers through the array to find the maximum profit in a single pass.

**Time complexity:** O(n)
**Space complexity:** O(1)

## Tags

- Array
- Two Pointers

## Link

🔗 [LeetCode - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
