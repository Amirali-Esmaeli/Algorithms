class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[k] = nums[i]
                k += 1
        return k

    