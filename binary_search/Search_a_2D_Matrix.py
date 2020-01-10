"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example:
    Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        L = 0
        R = len(matrix)-1
        if(R < 0):
            return False
        n = len(matrix[0])-1
        if(n< 0):
            return False
        while(L<= R):#注意等号，返回大于target的第一个数字class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        L = 0
        R = len(matrix)-1
        if(R < 0):
            return False
        n = len(matrix[0])-1
        if(n< 0):
            return False
        while(L<= R):
            middle= (L+R)/2
            if(target < matrix[middle][n]):
                R = middle-1
            elif(target > matrix[middle][n]):
                L = middle+1
            else:
                L = middle
                break
        if(L> len(matrix)-1 or target not in matrix[L]):
            return False
        else:
            return 
            middle= (L+R)/2
            if(target < matrix[middle][n]):
                R = middle-1
            elif(target > matrix[middle][n]):
                L = middle+1
            else:
                L = middle
                break
        if(L> len(matrix)-1 or target not in matrix[L]):
            return False
        else:
            return 
