# 0001. Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## Solutions

### ✅ Brute-force
Check all pairs of elements.

**Time complexity:** O(n²)  
**Space complexity:** O(1)

### ✅ HashMap (Optimal)
Use a dictionary to store the complement values.

**Time complexity:** O(n)  
**Space complexity:** O(n)

### ✅ Two Pointers (sorted with original indices)
Sort while keeping track of original indices, then use two pointers.

**Time complexity:** O(n log n)  
**Space complexity:** O(n)

## Tags

- Array
- Hash Table
- Two Pointers

## Link

🔗 [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)
