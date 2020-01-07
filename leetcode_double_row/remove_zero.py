class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L= 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                if(L != i):
                    m = nums[L]
                    nums[L]= nums[i]
                    nums[i]= 0
                L =L+1

