# Problem: Maximum Subarray
# Difficulty: Medium

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


class Solution:
    # Solution 1 - Brute Force O(n³)
    def max_subarray_brute_force(self, nums):
        best = nums[0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                current_sum = 0
                for k in range(i, j+1):
                    current_sum += nums[k]
                best = max(best,current_sum)
        return best

    # Solution 2 - Prefix Sum O(n²)
    def max_subarray_prefix(nums):
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        best = float('-inf')
        for i in range(n):
            for j in range(i, n):
                current_sum = prefix[j+1] - prefix[i]
                best = max(best, current_sum)
        return best

    # Solution 3 - Kadane’s Algorithm O(n)
    def max_subarray_kadane(nums):
        best = nums[0]
        current = nums[0]
        
        for x in nums[1:]:
            current = max(x, current + x)
            best = max(best, current)
        
        return best
