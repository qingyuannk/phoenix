'''
## 解题思路
这是我写的，虽然写出来了，但是感觉很不好
此处撰写解题思路

### 代码
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0
        R= 0
        M = 0
        a = -1
        while(R<= len(nums)):
            if(R<len(nums) and nums[R] == nums[L]):
                R = R+1
            else:
                if(R-L<=2):
                    if(L == M):
                        M = R
                    else:
                        a = R - L
                else:
                    if(L==M):
                        M = M+1
                    else:
                        a = 2
                while(a>0):
                    a= a-1
                    M = M+1
                    nums[M] = nums[L]
                    L = L+1
                L = R
                R =R+1
        return M+1
'''

#下面大神写的
def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for e in nums:
            if i < 2 or e != nums[i - 2]:
                nums[i] = e
                i += 1

        return i

