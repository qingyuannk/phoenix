### 解题思路
此处撰写解题思路
初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.

初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.

初始化当前考虑的元素序号 ：curr = 0.

While curr <= p2 :

若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。

若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。

若 nums[curr] = 1 ：将指针curr右移。

### 代码

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L = 0
        R = len(nums)-1
        i = 0
        while(i<=R):
            while(L< R and nums[L] == 0):
                L = L + 1
                i = i+1
            while(L<R and nums[R] == 2):
                R= R - 1
            if(R==L):
                break
            elif(i> L and nums[i] ==0):
                temp = nums[i]
                nums[i] = nums[L]
                nums[L] = temp
                L = L +1
            elif(i<R and nums[i] == 2):
                temp = nums[i]
                nums[i] = nums[R]
                nums[R] = temp
                R = R-1
            elif(nums[i] == 1):
                i = i +1
            else:
                continue
