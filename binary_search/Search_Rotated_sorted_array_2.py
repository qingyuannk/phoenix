"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
"""
def binary_search(nums,target):
    L = 0
    R = len(nums)-1
    while(L<= R):
        middle = (L +  R )/2
        if(nums[middle]<target):
            L = middle + 1
        elif(nums[middle] > target):
            R = middle -1
        else:
            return middle
    return (L+R)/2


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if(len(nums) == 0):
            return False
        L = 0
        R = len(nums)-1
        """

        与１比较起来主要是去重
        """
        while(L<R and nums[L] == nums[L+1]):
                L = L +1
        while(L<R and nums[R] == nums[R-1]):
                R = R-1
        while(nums[L] >= nums[R] and L != R):
            middle = (L+R)/2
            if(nums[middle]>nums[R]):
                L = middle +1
            else:
                R = middle
        print(nums[L],R)
        if( target<= nums[len(nums)-1]):
            m = binary_search(nums[L:len(nums)],target)
            m  =  L+m
        elif(nums[0]<= target):#
            m = binary_search(nums[0:L],target)
        else:
            m = -1
        print(m)
        if(m != -1 and nums[m] == target):
            return True
        else:
            return False

