def two_split(nums,target,lo,high):
    while(lo<=high):
        middle = (lo + high)/2
        if(nums[middle] < target):
            lo = middle+1
        elif(nums[middle]>target):
            high = middle-1
        else:
            return middle
    return lo
class Solution(object):


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums) -1
        lo = 0
        high=n
        if(n<0):
            return -1
        while(nums[lo]> nums[high]):
            middle = (lo+high)/2
            if(nums[middle]>nums[high]):
                lo = middle+1
            else:
                high = middle
        print(lo)
        if(nums[n]<target<=nums[lo-1]):
            m = two_split(nums,target,0,lo-1)
        elif(nums[lo]<target<=nums[n]):
            m = two_split(nums,target,lo,n)
        else:
            m = lo
        if(nums[m]==target):
            return m
        else:
            return -1
