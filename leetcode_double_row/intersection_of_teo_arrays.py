"""
Given two arrays, write a function to compute their intersection.
Example1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)
"""
收获:
集合可以进行交并差 & | - 运算
"""
