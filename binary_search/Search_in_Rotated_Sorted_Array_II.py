"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:
    [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


Given target = 5, return true.

Given target = 20, return false.
"""
"""
第一种写法并不好
考虑第一种写法，从右上角开始寻路
"""
def  binary_search(nums,target): 
    lo = 0
    high = len(nums)-1
    while(lo<=high):
        middle = (lo+high)/2
        if(nums[middle] < target):
            lo = middle +1
        elif(nums[middle]>target):
            high = middle -1
        else:
            return middle
    return (lo+high)/2

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        m = len(matrix)-1
        j = 0
        if( len(matrix)== 0 or len(matrix[0])==0):
            return False
        while(i<= m and 0 <= j ):
            j = binary_search(matrix[i],target)
            list_row = [x[j] for x in matrix]
            i = binary_search(list_row,target)
            if(matrix[i][j] == target):
                return True
            else:
                i = i+1
                j = j-1
        return Falsedef  binary_search(nums,target): 
    lo = 0
    high = len(nums)-1
    while(lo<=high):
        middle = (lo+high)/2
        if(nums[middle] < target):
            lo = middle +1
        elif(nums[middle]>target):
            high = middle -1
        else:
            return middle
    return (lo+high)/2

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        m = len(matrix)-1
        j = 0
        if( len(matrix)== 0 or len(matrix[0])==0):
            return False
        while(i<= m and 0 <= j ):
            j = binary_search(matrix[i],target)
            list_row = [x[j] for x in matrix]
            i = binary_search(list_row,target)
            if(matrix[i][j] == target):
                return True
            else:
                i = i+1
                j = j-1
        return False
def  binary_search(nums,target): 
    lo = 0
    high = len(nums)-1
    while(lo<=high):
        middle = (lo+high)/2
        if(nums[middle] < target):
            lo = middle +1
        elif(nums[middle]>target):
            high = middle -1
        else:
            return middle
    return (lo+high)/2

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        m = len(matrix)-1
        j = 0
        if( len(matrix)== 0 or len(matrix[0])==0):
            return False
        while(i<= m and 0 <= j ):
            j = binary_search(matrix[i],target)
            list_row = [x[j] for x in matrix]
            i = binary_search(list_row,target)
            if(matrix[i][j] == target):
                return True
            else:
                i = i+1
                j = j-1
        return False
"""
寻路
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j = j + 1
            else:
                i = i - 1
        return False
