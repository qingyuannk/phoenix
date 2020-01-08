"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

"""
class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        L = nums[0]
        R = nums[0]
        while(1):
            j = L
            i = nums[R]
            L = nums[j]
            R = nums[i]
            if(i == j):
                j = 0
                L = nums[j]
                while(i!=j):
                    j = L
                    i = R
                    L= nums[j]
                    R = nums[i]
                break
        return i
