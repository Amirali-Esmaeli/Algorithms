class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_reach = 0
        max_value = 0
        count = 0
        n = len(nums)
        
        for i in range(n):
            max_value = max(max_value,i + nums[i])
            if i == max_reach and i != len(nums) - 1:
                max_reach = max(max_reach, max_value)
                count += 1
        return count

        