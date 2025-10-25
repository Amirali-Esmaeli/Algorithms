# Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit.  
Add the two numbers and return the sum as a linked list.

**Example:**

Input:  
l1 = [2,4,3]  
l2 = [5,6,4]  

Output:  
[7,0,8]

**Explanation:**  

342 + 465 = 807

## Solutions

### ✅ Iterative (Optimal)
- Traverse both linked lists node by node.
- At each step, sum the corresponding digits and carry.
- Create a new node for each digit of the result.
- Continue until both lists and carry are processed.

**Time complexity:** O(n)  
**Space complexity:** O(n)  
*(where n is the length of the longer list)*

## Tags

- Linked List
- Math
- Simulation

## Link

🔗 [LeetCode - Two Sum](https://leetcode.com/problems/add-two-numbers/)
