# Problem: Contains Duplicate
# Difficulty: Easy

# Input: num = [1,2,3,1]
# Output: true


class Solution:
    # Solution 1 - Set O(n)
    def contains_duplicate_set(self, nums):
        return len(nums) != len(set(nums))

    # Solution 2 - Hash Set (O(n))
    def contains_duplicate_hash_set(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Solution 3 - Sort O(n log n)
    def contains_duplicate_sort(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
