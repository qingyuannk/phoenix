class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxs  = nums[0]
        imins   =  1
        imax   = 1
        res = 0
        for i in range(n):
            if nums[i] < 0:
                tmp = imax 
                imax = imins
                imins= tmp

            imax = max(imax * nums[i],nums[i])
            imins = min (imins * nums[i],nums[i])
            maxs = max(maxs,imax)

        return maxs


"""
记录最小值,是因为如果偶数个负数出现,算法还能成功
max(imax*nums[i],nums[i])
min(imin*nums[i],nums[i])
"""
