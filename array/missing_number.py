"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = range(0,n+1)
        for e in nums:
            a[e] = n+1
        print(a)
        for v in a:
            if v != n+1:
                return v

