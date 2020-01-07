lass Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)+1
        L = 0
        R = 0
        sums = 0
        while(L<len(nums)):
            if(sums<s):
                if(R ==len(nums)):
                    break
                sums += nums[R]
                R = R + 1
            else:
                if(a >= (R-L)):
                    a = R-L
                sums -= nums[L]
                L = L +1
        if a == len(nums)+1:
            return 0
        else:
            return a
