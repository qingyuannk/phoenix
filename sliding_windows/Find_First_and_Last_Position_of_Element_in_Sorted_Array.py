"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
"""
"""
秀一把二分查找
"""
def binary_search(nums,target):
    lo = 0
    high =len(nums)-1
    while(lo<= high):
        middle = (lo+high)/2
        if(nums[middle]< target):
            lo = middle +1
        else:
            high = middle -1
    return (lo+high)/2



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums) == 0):
            return [-1,-1]
        n = binary_search(nums,target)
        m = binary_search(nums,target+1)
        if(n+1 > m):
            return [-1,-1]
        else:
            retu
