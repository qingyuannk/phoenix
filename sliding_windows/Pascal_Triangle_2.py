"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        for i in range(rowIndex+1):
            now = [1]*(i+1)
            if i >= 2:
                for n in range(1,i):
                    now[n] = pre[n] + pre[n-1]
            pre = now
        return now
