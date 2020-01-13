"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example1:
    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

"""
环状替换
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        if(n == 0):
            return
        k = k % n
        start = 0
        while(count<n):
            now = start
            now_value = nums[start]
            while(1):
                current = (now + k)%n
                tmp = nums[current]
                nums[current] = now_value
                now = current
                now_value = tmp
                count = count + 1
                if(current == start):
                    break
            start = start+1
