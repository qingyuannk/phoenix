"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
    Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""
"""
二进制解法
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        L = 0
        R = x
        if(x==1):
            return x
        while(1):
            i = (L + R)/2
            print(i)
            if(i*i < x):
                if((i*1)^2 >x):
                    return i
                else:
                    L  = i
            elif(i*i  >x):
                if((i-1)*(i-1) < x):
                    print(i)
                    return i-1
                else:
                    R = i
            else:
                return i
"""
牛顿法
"""
class Solution:

    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

