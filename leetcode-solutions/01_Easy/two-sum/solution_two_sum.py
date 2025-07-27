# Problem: Two Sum
# Difficulty: Easy

# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [0, 1]


# Solution 1 - Brute Force (O(n^2))
class Solution:
    def twoSum(self, nums, target):
        a = len(nums)
        for i in range(a):
            for j in range(i + 1, a):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution 2 - Hash Map (O(n))
class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]


# Solution 3 - Two Pointers After Sorting (O(n log n))
class Solution:
    def twoSum(self, nums, target):
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left][1] + nums[right][1]
            if total == target:
                return [nums[left][0], nums[right][0]]
            elif total < target:
                left += 1
            else:
                right -= 1
