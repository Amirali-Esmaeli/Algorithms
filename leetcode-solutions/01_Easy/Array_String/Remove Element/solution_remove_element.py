class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for index in range(len(nums)):
            if nums[index] == val:
                continue
            else:
                nums[k] = nums[index]
                k += 1
        return k


        