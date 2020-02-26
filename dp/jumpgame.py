"""
递归动态规划
"""
class Solution(object):
    def canJump(self,nums):
        if len(nums) == 1:
            return True
        for i in range(1,nums[0]+1):
            if i <= len(nums):
                if self.canJump(nums[i:]):
                    return True
            else:
                return True
        return False

"""
备忘录递归动态规划
"""
class Solution(object):
    def canJump(self,nums):
        n = len(nums)
        if n == 1:
            return True
        a = [0] * n 
        a[n-1] = 1
        position = 0
        return self.canJumps(nums,a,position)
        
    def canJumps(self,nums,a,position):
        print(nums[position])
        if a[position] != 0:
            print(1)
            if a[position] == 1:
                return True
            else:
                return False
        print(position)
        furjump = min(nums[position]+position,len(nums)-1)
        for i in range(position+1,furjump+1):
            if i <= len(nums):
                if self.canJumps(nums,a,i):
                    a[i] = 1
                    return True
            else:
                return True
        a[position]=-1
        return False
"""
自底向上动态规划
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        memo = [0] * n
        memo[n-1] = 1
        m = n - 2
        while m>=  0:
            furjump = min(m+nums[m],n)
            print(m,furjump)
            for j in range(m+1,furjump+1):
                if (memo[j] == 1):
                    memo[m]= 1
                    break
            m = m -1
        print(memo)
        return memo[0] == 1
"""
贪心算法
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 2
        lasted = len(nums)- 1
        while n >= 0:
            if (n + nums[n]>= lasted):
                lasted= n
            n = n - 1
        return lasted== 0

