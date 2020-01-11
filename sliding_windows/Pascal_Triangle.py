"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

"""
"""
对比杨辉三角２
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = []
        sums = 0
        for i in range(numRows):
            b= [1]
            if len(a) == 0:
                a.append(b)
            else:
                for j in range(len(a[i-1])):
                    if  j == len(a[i-1])-1:
                        b.append(1)
                        a.append(b)
                    else:
                        sums = a[i-1][j]+a[i-1][j+1]
                        b.append(sums)
        return a
