### 解题思路
此处撰写解题思路

### 
'''
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L =  0
        sums = 0
        max_sums = nums[0]
        for i in range(len(nums)):  
            if(sums < 0):
                L = i
                sums = 0
            sums = sums + nums[i]
            if(sums> max_sums):
                max_sums = sums
        return  max_sums
```
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sums = nums[0]
        sums = 0
        for num in nums:
            if(sums > 0):
                sums += num
            else:
                sums = num
            if(sums > max_sums):
                max_sums = sums
        return max_sums
