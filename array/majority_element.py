"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
Example:
    Input: [3,2,3]
    Output: 3
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        ant = 0
        for e in nums:
            if(count == 0):
                ant = e
                count = count +1
            else:
                if(ant == e):
                    count = count +1
                else:
                    count = count - 1
        return ant

